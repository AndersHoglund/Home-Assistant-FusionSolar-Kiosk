"""API client for FusionSolar Kiosk."""
import logging
import html
import json

from .const import (
    ATTR_DATA,
    ATTR_FAIL_CODE,
    ATTR_SUCCESS,
    ATTR_DATA_REALKPI,
    ATTR_TOTAL_LIFETIME_ENERGY,
)

from requests import get

_LOGGER = logging.getLogger(__name__)

lastGoodLifetimeEnergy = {}

class FusionSolarKioksApi:
    def __init__(self, host):
        self._host = host

    def getRealTimeKpi(self, id: str):

        global lastGoodLifetimeEnergy

        url = self._host + '/rest/pvms/web/kiosk/v1/station-kiosk-file?kk=' + id
        headers = {
            'accept': 'application/json',
        }

        try:
            response = get(url, headers=headers)
            # _LOGGER.debug(response.text)
            jsonData = response.json()

            if not jsonData[ATTR_SUCCESS]:
                raise FusionSolarKioskApiError(f'Retrieving the data failed with failCode: {jsonData[ATTR_FAIL_CODE]}, data: {jsonData[ATTR_DATA]}')

            # convert encoded html string to JSON
            jsonData[ATTR_DATA] = json.loads(html.unescape(jsonData[ATTR_DATA]))
            _LOGGER.debug('Received data for ' + id + ': ')
            _LOGGER.debug(jsonData[ATTR_DATA][ATTR_DATA_REALKPI])

            # Validate response
            if id not in lastGoodLifetimeEnergy:
                lastGoodLifetimeEnergy[id] = 0

            if jsonData[ATTR_DATA][ATTR_DATA_REALKPI][ATTR_TOTAL_LIFETIME_ENERGY] < lastGoodLifetimeEnergy[id]:
                jsonData[ATTR_DATA][ATTR_DATA_REALKPI][ATTR_TOTAL_LIFETIME_ENERGY] = lastGoodLifetimeEnergy[id]
                _LOGGER.debug(jsonData[ATTR_DATA][ATTR_DATA_REALKPI])
            else:
                lastGoodLifetimeEnergy[id] = jsonData[ATTR_DATA][ATTR_DATA_REALKPI][ATTR_TOTAL_LIFETIME_ENERGY]

            return jsonData[ATTR_DATA][ATTR_DATA_REALKPI]

        except FusionSolarKioskApiError as error:
            _LOGGER.error(error)
            _LOGGER.debug(response.text)

        except FusionSolarKioskApiError as error:
            _LOGGER.error(error)
            _LOGGER.debug(response.text)
    
        return {
            ATTR_SUCCESS: False
        }

class FusionSolarKioskApiError(Exception):
    pass

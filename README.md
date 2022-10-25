# Home Assistant FusionSolar Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

**IMPORTANT: This integration is not longer maintained**. You can upgrade to the newer [FusionSolar](https://github.com/tijsverkoyen/HomeAssistant-FusionSolar)-integration. 
Which not only supports Kiosk but also the use of an OpenAPI account. The later has actually realtime info.

Integrate FusionSolar into you Home Assistant.

FusionSolar has a kiosk mode. When this kiosk mode is enabled we can access 
data about our plants through a JSON REST api.

{% if installed %}
{% if version_installed.replace("v", "").replace(".","") | int < 303  %}
### No longer maintained
**This integration is not longer maintained.**
I strongly suggest to upgrade to the newer [FusionSolar](https://github.com/tijsverkoyen/HomeAssistant-FusionSolar)-integration. 
{% endif %}

{% if version_installed.replace("v", "").replace(".","") | int < 300  %}
## Breaking Changes
### Use the full kiosk url (since v3.0.0)
Your current configuration should be updated. Before v3.0.0 we used the kiosk id. 
Starting with v3.0.0 the full kiosk url should be used:

    sensor:
      - platform: fusion_solar_kiosk
        kiosks:
          - url: "REPLACE THIS WITH THE KIOSK URL"
            name: "A readable name for the plant"

See the "Configuration" section for more details
{% endif %}
{% endif %}

## Remark
**In kiosk mode the "realtime" data is not really realtime, it is cached at FusionSolars end for 30 minutes.**

If you need more accurate information you can use [Home Assistant FusionSolar OpenAPI Integration](https://github.com/olibos/Home-Assistant-FusionSolar-OpenApi/) by @olibos. This integration requires an OpenAPI account.

## Installation
At this point the integration is not part of the default HACS repositories, so
you will need to add this repository as a custom repository in HACS.

When this is done, just install the repository.


## Configuration

The configuration of this integration happens in a few steps:

### Enable kiosk mode
1. Sign in on the Huawei FusionSolar portal: [https://eu5.fusionsolar.huawei.com/](https://eu5.fusionsolar.huawei.com/).
2. Select your plant if needed.
2. At the top there is a button: "Kiosk", click it.
3. An overlay will open, and you need to enable the kiosk view by enabling the toggle.
4. Note down the url that is shown.

### Add into configuration
Open your `configuration.yaml`, add the code below:

    sensor:
      - platform: fusion_solar_kiosk
        kiosks:
          - url: "REPLACE THIS WITH THE KIOSK URL"
            name: "A readable name for the plant"

### Use secrets
I strongly advise to store the unique urls as a secret. The kiosk url is public, 
so anybody with the link can access your data. Be careful when sharing this.

More information on secrets: [Storing secrets](https://www.home-assistant.io/docs/configuration/secrets/).

### Multiple plants
You can configure multiple plants:

    sensor:
      - platform: fusion_solar_kiosk
        kiosks:
            - url: "KIOSK URL XXXXX"
              name: "A readable name for plant XXXXX"
            - url: "KIOSK URL YYYYY"
              name: "A readable name for plant YYYYY"

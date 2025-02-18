---
card: true
name: Atlas ORP
field:
  - water
type:
  - external
target:
  - orp
feature_img: /assets/images/atlas-scientific-orp.jpg
feature_img_credit: "Atlas Scientific"
excerpt: "An ORP probe is a passive device that detects a current generated from the oxidation or reduction of chemical substances in water."
internal:
  proofread: false
  links: false
  images: false
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

## Working principle

## Usage and considerations

No particular consideration for the probe, other than it is very delicate:

![](/assets/images/water/atlas-ph-warning.png)

!!! danger "Storage solution"
    This probe needs storage solution in a small soaker bottle to prevent it from drying out.

    If the probe is not being used you need to put the soaker bottle back on.

### Calibration

{{ get_snippet_rel('docs/includes/pre-calibration-water-stations.md')}}

You only need to perform a single point calibration. You can use any calibrated solution, as long as it's within your sensor range. Atlas uses a 225mV calibration.

!!! info "Datasheet"
    Here you can find the [datasheet](https://files.atlas-scientific.com/ORP_EZO_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 49

    **Example commands**

    ```
    control redox com,r
    control redox com,cal
    control redox com,cal,[value]
    control redox com,cal,clear
    control redox com,cal,?
    ```

#### Single point calibration

![](/assets/images/water/atlas_orp_cal_process.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control redox com,r
    225
    control redox com,r
    224
    ...
    ```

* Issue calibration command

    ```
    control redox com,cal,[value of ORP]
    ```

!!! info "Example at 25°C"

    ```
    control redox com,cal,225
    ```

{{ get_snippet_rel("docs/includes/water-probes-reset.md") }}
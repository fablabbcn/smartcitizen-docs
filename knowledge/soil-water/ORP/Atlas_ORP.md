<!-- Source: https://docs.smartcitizen.me/knowledge/soil-water/ORP/Atlas_ORP/ -->

# Atlas ORP

An ORP probe is a passive device that detects a current generated from the oxidation or reduction of chemical substances in water.

![](https://docs.smartcitizen.me/assets/images/atlas-scientific-orp.jpg){.banner-box}

_Image Credit: **Atlas Scientific**_{.image-credit-banner-box}

## Working principle

The ORP probe measures the voltage between a platinum (or gold) measuring electrode and a reference electrode. The EZO ORP circuit reads this voltage in a range of **-1020 mV to +1020 mV**, with an accuracy of ±1 mV [^1].

## Usage and considerations

The following metrics are available:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Oxidation-reduction potential | `Atlas Redox potential` | mV | [164](https://api.smartcitizen.me/v0/sensors/164) |

No particular consideration for the probe, other than it is very delicate:

![](https://docs.smartcitizen.me/assets/images/water/atlas-ph-warning.png)

!!! danger "Storage solution"
    This probe needs storage solution in a small soaker bottle to prevent it from drying out.

    If the probe is not being used you need to put the soaker bottle back on.

### Calibration


!!! warning
    When calibrating **don't use the normal `read sensor` command**, this command applies temperature/salinity compensation, calibration should be done without any compensation. Instead you should use `control sensorName com,r` and that will return the raw metrics that sensor can provide. On the documentation of each sensor calibration procedure we describe the format of this metrics.

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

![](https://docs.smartcitizen.me/assets/images/water/atlas_orp_cal_process.png)

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


### Factory reset procedure

!!! info "Why is this needed?"
    You may need to do a factory reset for water sensors for different reasons. However, the most common case is a wrong calibration process and it's very much related to a wrongful automatic temperature compensation of the sensor while calibrating the sensor.

    To explain further: EC, DO and pH sensor readings are automatically compensated by temperature readings. If there is an existing temperature correction in the EZO driver, or there is a correction in the middle of the calibration process, the data available for the calibration process will be invalid. Follow the steps below to be make sure there is no correction while you calibrate the probes.

Each EZO driver has it's independent calibration and status. This process needs to be done per **_driver_** (i.e. per EZO metric). To make a factory reset procedure for the EZO drivers follow the steps below:

1. Make sure that the [Smart Citizen Data](https://docs.smartcitizen.me/hardware/boards/data-board.md) board will not take any readings while you follow the calibration process. The best option is to reset the configuration to the defaults. Make sure you [back-up your information](https://docs.smartcitizen.me/guides/firmware/upgrading-the-firmware.md#make-a-back-up-of-your-info/) before:

    - The config command will output your current configuration. Copy it and keep it safe:

    ```
    config
    ```

    - Then issue the default configuration:

    ```
    config -defaults
    ```

    - The LED should be red now (the Data Board is in [Setup mode](https://docs.smartcitizen.me/hardware/kit/features.md#setup-mode))

2. Issue the factory reset command to the _driver_ in question. For instance, for the _conductivity_ one:

    ```
    control cond com factory
    0
    ```

3. Now you can check what the status of the device is:

    ```
    control cond com cal,?
    ?CAL,0
    ```

4. Reset the kit

5. Follow the calibration process as you would normally would.

6. Reconfigure the kit using the `config` command, by putting back the information you backed-up before:

    ```
    config -mode ...
    ```

!!! danger
    After finishing the calibration process **restart your SCK** to start from a clean state.

## Resources

- [EZO ORP datasheet](https://files.atlas-scientific.com/ORP_EZO_Datasheet.pdf)

### References

[^1]:
    Atlas Scientific. “EZO-ORP Embedded ORP Circuit - Datasheet.” https://files.atlas-scientific.com/ORP_EZO_Datasheet.pdf.
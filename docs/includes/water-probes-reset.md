# Water probes reset

### Factory reset procedure

!!! info "Why is this needed?"
    You may need to do a factory reset for water sensors for different reasons. However, the most common case is a wrong calibration process and it's very much related to a wrongful automatic temperature compensation of the sensor while calibrating the sensor.

    To explain further: EC, DO and pH sensor readings are automatically compensated by temperature readings. If there is an existing temperature correction in the EZO driver, or there is a correction in the middle of the calibration process, the data available for the calibration process will be invalid. Follow the steps below to be make sure there is no correction while you calibrate the probes.

Each EZO driver has it's independent calibration and status. This process needs to be done per **_driver_** (i.e. per EZO metric). To make a factory reset procedure for the EZO drivers follow the steps below:

1. Make sure that the [Smart Citizen Data](/hardware/boards/data-board/) board will not take any readings while you follow the calibration process. The best option is to reset the configuration to the defaults. Make sure you [back-up your information](/guides/firmware/upgrading-the-firmware/#make-a-back-up-of-your-info/) before:

    - The config command will output your current configuration. Copy it and keep it safe:

    ```
    config
    ```

    - Then issue the default configuration:

    ```
    config -defaults
    ```

    - The LED should be red now (the Data Board is in [Setup mode](/hardware/kit/features/#setup-mode))

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
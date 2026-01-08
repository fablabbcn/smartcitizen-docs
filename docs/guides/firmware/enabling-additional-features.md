# Enabling additional features

The SCK has certain features that are disabled by default in order to save flash memory. However these features can be enabled with simple flags at compilation time.

The available features range from enabling additional [supported sensors](/knowledge/#auxiliary-connector/) to other features like the enabling the [oled display](/hardware/addons/oled-screen/).

## Process

To enable these features, you need to compile the firmware with the relevant compile flags. You can do this in two ways:

- Add firmware compile flags to `platformio.ini` in the `sam` directory. For instance, for the `sck23_air`, to add the [oled display](/hardware/addons/oled-screen/):

    ```
    [env:sck23_air]
    build_flags =
        !sh ../tools/git-rev.sh -e sck23_air
        -D SCK23_AIR
        -D WITH_SENSOR_GROVE_OLED
    ```

- Alternatively, you can also uncomment the relevant line in the [Sensors.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/lib/Sensors/Sensors.h) file. In this case, the file should read:

    ```
    #define WITH_SENSOR_GROVE_OLED  // Saves 2496 bytes
    ```

## List of features

Most features are listed in the [Sensors.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/lib/Sensors/Sensors.h) file.

Different versions of the SCK have different features enabled by default. Additionally, the field of measurement (air or water), has different sensors enabled. These versions are defined with the `SCK21_AIR`, `SCK22_AIR`, `SCK23_AIR`, `SCK_WATER` and `SCK2`, the latter being a boilerplate for testing. Other configurations are possible by defining custom flags as required. Since the `_WATER` sensors can be used with _any_ [data board](/hardware/boards/data-board/) (SCK2.1 onwards), they are independent of the hardware version.

In the `Sensors.h` file, different configuration features are enabled for different versions of the SCK (`SCK*` flags), with a list of all available flags included in the `SCK2` section.

### Sensor flags

Features starting with `WITH_` involve sensors or additional boards that are only enabled by default on certain configurations. A complete list is available in [Sensors.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/lib/Sensors/Sensors.h). For instance:

```
#define WITH_SEN5X    // Enables sensirion SEN5X series
#define WITH_URBAN    // Enables the Urban board
#define WITH_MPL      // Enables MPL pressure sensor
#define WITH_AS7331   // Enables UV sensor
#define WITH_SCD30    // Enables CO2 sensor
#define WITH_ADS1X15  // Enables ADC
#define WITH_SFA30    // Enables HCHO sensor
#define WITH_GPS      // Enables GPS
#define WITH_EXT_TEMP // Enables External temperature sensor
```

### Additional features

Default [temperature calibration](https://forum.smartcitizen.me/t/new-firmware-feature-temperature-and-relative-humidity-corrections/2018) parameters (in the form of an offset) can be defined with the following:

```
#define URBAN_T_OFFSET 0
#define URBAN_RH_OFFSET 0
```

!!! warning "Better use the shell"
    The calibration parameters can be changed directly using the [shell](https://forum.smartcitizen.me/t/new-firmware-feature-temperature-and-relative-humidity-corrections/2018).
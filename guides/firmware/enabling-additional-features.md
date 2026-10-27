<!-- Source: https://docs.smartcitizen.me/guides/firmware/enabling-additional-features/ -->

# Enabling additional features

The SCK has certain features that are disabled by default in order to save flash memory. However these features can be enabled with simple flags at compilation time.

The available features range from enabling additional [supported sensors](https://docs.smartcitizen.me/knowledge.md) to other features like enabling the [oled display](https://docs.smartcitizen.me/hardware/addons/oled-screen.md).

!!! info "Firmware version"
    This page refers to firmware **V0.9.12** onwards. In previous versions, the flags were named `WITH_*` instead of `SCK_WITH_*`.

## Process

To enable these features, you need to [compile the firmware](https://docs.smartcitizen.me/guides/firmware/edit-the-firmware.md) with the relevant compile flags. You can do this in two ways:

- Add the flags to the environment you are compiling in the `platformio.ini` file, in the `sam` directory. For instance, to add the [SPS30](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SPS30.md) to the `sck23_air` environment:

    ```
    [env:sck23_air]
    extends = env_air_common
    build_flags =
        ${env_common.build_flags}
        !sh ../tools/git-rev.sh -e sck23_air
        -D SCK23_AIR
        -D SCK_WITH_SPS30
    ```

- Alternatively, you can add a `#define` line inside the block of your configuration at the top of the [Sensors.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/lib/Sensors/Sensors.h) file. For instance, for the `SCK23_AIR` configuration:

    ```
    #ifdef SCK23_AIR
    #define SCK_WITH_SEN5X
    ...
    #define SCK_WITH_SPS30
    #endif
    ```

!!! warning "Libraries"
    Each environment in `platformio.ini` only includes the libraries needed by the sensors it enables by default (under `lib_deps`). If you enable a sensor that is not enabled by default in your environment, make sure that its library is also available. For instance, the libraries for the [SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md) and the [AS7341](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7341.md) are only listed in the `sck23_air` environment. If you want to use them with another configuration, copy them to the `lib_deps` of that environment.

!!! warning "Flash memory"
    The flash memory of the SCK is limited. Enabling many additional features at the same time might make the firmware too big to fit. If that happens, disable the features you don't need.

## List of features

Different versions of the SCK have different features enabled by default. Additionally, the field of measurement (air or water) has different sensors enabled. These configurations are defined with the `SCK21_AIR`, `SCK22_AIR`, `SCK23_AIR` and `SCK_WATER` flags, each of them with its own environment in `platformio.ini` (`sck21_air`, `sck22_air`, `sck23_air` and `sck_water`). Since the `_WATER` sensors can be used with _any_ [data board](https://docs.smartcitizen.me/hardware/boards/data-board.md) (SCK2.1 onwards), they are independent of the hardware version.

The `Sensors.h` file defines which features are enabled for each configuration:

| Flag | SCK21_AIR | SCK22_AIR | SCK23_AIR | SCK_WATER |
|:- |:-: |:-: |:-: |:-: |
| `SCK_WITH_URBAN` | ✓ | ✓ | ✓ | |
| `SCK_WITH_NOISE` | ✓ | ✓ | ✓ | |
| `SCK_WITH_PMS` | ✓ | | | |
| `SCK_WITH_CCS811` | ✓ | | | |
| `SCK_WITH_SEN5X` | | ✓ | ✓ | |
| `SCK_WITH_MPL` | ✓ | | ✓ | |
| `SCK_WITH_LPS33` | | ✓ | | |
| `SCK_WITH_AS7331` | | ✓ | ✓ | |
| `SCK_WITH_ADS1X15` | ✓ | ✓ | ✓ | |
| `SCK_WITH_SCD30` | ✓ | ✓ | ✓ | |
| `SCK_WITH_SFA30` | ✓ | ✓ | ✓ | |
| `SCK_WITH_EXT_TEMP` | ✓ | ✓ | ✓ | |
| `SCK_WITH_SCD4X` | | | ✓ | |
| `SCK_WITH_AS7341` | | | ✓ | |
| `SCK_WITH_GPS` | ✓ | ✓ | ✓ | ✓ |
| `SCK_WITH_ATLAS` | | | | ✓ |

### Sensor flags

Features starting with `SCK_WITH_` involve sensors or additional boards. Besides the ones in the table above, the following flags are available, but not enabled in any of the default configurations:

```
#define SCK_WITH_SPS30          // Sensirion SPS30 PM sensor
#define SCK_WITH_BME68X         // Bosch BME680 environmental sensor
#define SCK_WITH_GASES_BOARD    // SCK Gases Board for Alphasense sensors
#define SCK_WITH_GROVE_I2C_ADC  // Seeed Grove I2C ADC
#define SCK_WITH_INA219         // TI INA219 current sensor
#define SCK_WITH_DS18B20        // DS18B20 temperature sensor (via DS2482 I2C bridge)
#define SCK_WITH_DALLAS_TEMP    // Dallas temperature sensor directly on the AUX connector
#define SCK_WITH_CHIRP          // Catnip Chirp soil moisture sensor
#define SCK_WITH_RANGE          // VL6180x range sensor
```

A complete list is available in [Sensors.h](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/lib/Sensors/Sensors.h).

### Oled display

The [oled display](https://docs.smartcitizen.me/hardware/addons/oled-screen.md) is enabled with the `SCK_WITH_SENSOR_GROVE_OLED` flag. Since it is a common option, `platformio.ini` already includes an environment with it for each configuration: `sck21_air_oled`, `sck22_air_oled`, `sck23_air_oled` and `sck_water_oled`.

### Additional features

Default [temperature calibration](https://forum.smartcitizen.me/t/new-firmware-feature-temperature-and-relative-humidity-corrections/2018) parameters (in the form of an offset) are defined for each configuration with the following:

```
#define URBAN_T_OFFSET -1.0
#define URBAN_RH_OFFSET 3.5
```

!!! warning "Better use the shell"
    The calibration parameters can be changed directly using the [shell](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md#modify-temperature-and-relative-humidity-offset), without recompiling the firmware.
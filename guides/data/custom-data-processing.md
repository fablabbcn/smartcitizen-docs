<!-- Source: https://docs.smartcitizen.me/guides/data/custom-data-processing/ -->

# Data processing

Some sensors need their data to be processed after the readings are collected. For instance, the [electrochemical sensors](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md) only report the raw voltages of their electrodes, and the pollutant concentrations are calculated afterwards. There are two ways to get your data processed:

1. **[Processing by Smart Citizen](#processing-by-smart-citizen)**: we take care of it, periodically and automatically, with our default algorithms. They run in [Smart Citizen Flows](https://flows.smartcitizen.me), using the processing functions of [`scdata`](https://github.com/fablabbcn/smartcitizen-data/).
2. **[Processing it yourself](#processing-it-yourself)**: if you want to try other algorithms, you can use the same tools we use, on your own computer.

!!! info "What we run"
    The automatic processing only uses our default algorithms. If you need a different processing, you can run it yourself with the tools described below. In that case, it is not automatic, and the results are not published on the platform.

!!!info "Too confusing?"
    [Contact us](mailto:support@smartcitizen.me) and/or open a topic on the [forum](https://forum.smartcitizen.me) and we will try to help!

## Processing by Smart Citizen

Smart Citizen Flows processes the devices that have a `postprocessing` field with a `hardware_url`. You can check it by visiting `https://api.smartcitizen.me/v0/devices/<device-id>`, where `<device-id>` is the number that follows `https://smartcitizen.me/kits/` in the url of your device.

!!! info "How to do it?"
    Visit [these instructions](https://docs.smartcitizen.me/guides/data/handling-calibration-data.md) to store the `postprocessing` of your device.

The `hardware_url` points to a **hardware** description in Flows, with the information needed to process the data: which **blueprints** (algorithms) to use, and which **calibration data** applies to the sensors of the device. The `hardware_url` can be the name of the hardware (e.g. `SCAS210022`, normally the hardware ID on the sticker of the device), or a url ending in `hardware/<name>.json`. If the hardware is not in Flows, the device is not processed.

All this processing metadata (hardware, blueprints, calibrations and sensor names) is public, at [`https://flows.smartcitizen.me/api/v1/`](https://flows.smartcitizen.me/api/v1/). We keep it up to date: the hardware of the units we provide is already in Flows. If something is wrong or missing, [contact us](mailto:support@smartcitizen.me).

### Hardware

A hardware description looks like this (`https://flows.smartcitizen.me/api/v1/hardware/SCAS210022`):

```
{
  "name": "SCAS210022",
  "blueprints": ["sc_air"],
  "description": "1PMS5003-2ELEC-AFE",
  "comment": null,
  "forwarding": null,
  "parameters": {},
  "versions": [
    {
      "ids": {
        "AS_48_32": "214240830",
        "AS_49_10": "212741109",
        "PT_49_23": "10-001222"
      },
      "from": "2021-02-08",
      "to": null
    }
  ],
  "url": "https://flows.smartcitizen.me/api/v1/hardware/SCAS210022.json"
}
```

- `blueprints`: the names of the blueprints that process the data of the devices with this hardware (see [below](#blueprints)), at most one of each kind.
- `description`: a brief description of the hardware.
- `versions`: the history of the sensors mounted in the hardware. Sensors can be replaced over time, so each version has the dates during which it was valid (`from` and `to`, `null` if it is still valid) and the `ids` of its sensors.
- `parameters`: parameters of the processing functions, to override the ones in the blueprint for the devices with this hardware (e.g. `{"O3": {"function": "alphasense_803_04"}}`).
- `comment` and `forwarding`: optional notes, and where the data is forwarded to.

In the `ids` field, the keys define the type of sensor and where it is connected, and the values are the ids of the sensors, normally their serial number:

- `AS` is an Alphasense electrochemical sensor, followed by the I2C address of the ADC and its channels. For instance, `AS_48_32` is an Alphasense sensor connected to the ADC with address `0x48`, with its _working electrode_ on channel 3 and its _auxiliary electrode_ on channel 2.
- `PT` is a PT1000 temperature probe on an Alphasense AFE board (e.g. `PT_49_23`), and its value is the id of the AFE board.

The calibration data of each sensor (e.g. the sensitivities and zeros provided by Alphasense) is in Flows too: `https://flows.smartcitizen.me/api/v1/calibrations/<sensor-id>`.

### Blueprints

A blueprint defines the **channels** to calculate from the readings of the device: which function calculates each channel, with which arguments, and which channels it depends on. Each channel with an `id` and `"post": true` is published on the platform with that sensor id. For instance, this is how NO2 is calculated from the electrodes of the sensor, following the [Alphasense Application Note 803-04](https://docs.smartcitizen.me/assets/notes/alphasense-an-803-04-zero-offset.pdf):

```
{
  "name": "NO2",
  "description": "Calculation of NO2 based on AAN 803-04",
  "id": 153,
  "kwargs": {
    "ae": null,
    "alphasense_id": null,
    "t": "EC_SENSOR_TEMP",
    "we": null
  },
  "post": true,
  "function": "alphasense_803_04",
  "unit": "ppb",
  "depends_on": ["NO2_WE", "NO2_AE", "EC_SENSOR_TEMP"]
}
```

The arguments that are `null` are filled in with the hardware: the electrodes are read from the ADC channels of the `AS` sensor whose id is an NO2 sensor, and `alphasense_id` is its id. Blueprints also define **health checks** (gaps, implausible values, flat values and outliers), which run on the processed data. The list of blueprints is at [`https://flows.smartcitizen.me/api/v1/blueprints`](https://flows.smartcitizen.me/api/v1/blueprints).

Each blueprint has a kind, which defines how Flows runs it:

| Kind | Example | Processing in Flows |
|:- |:- |:- |
| `process` | `sc_air` | Every 3 hours, processes the latest readings of the device (up to 1000) and publishes the results on the platform. |
| `long` | `sc_air_baseline` | Weekly, processes a long window of the device data (90 days by default), with algorithms that need months of data, such as baselines. The results are **not** published on the platform. |
| `backup` | `backup` | Backs up the data of the device. |

A hardware has a `process` blueprint, a `long` one, or both. It can also have a `backup` one, instead of the `long` one, since long processing already backs up the data. Devices are only processed with the blueprints of their hardware. The `long` processing is used in research projects and is not offered commercially (see the [electrochemical sensors data processing](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md#data-processing)).

### Results and device health

The results of the `process` blueprints are published on the platform, as any other sensor of your device. Researchers can sign in to Flows with their Smart Citizen account to see, for the devices they own, their hardware and calibrations, the health of each device, and the results of the `long` processing.

## Processing it yourself

If you want to try other algorithms, you can process the data on your own computer. This processing is up to you: it is not automatic, and the results are not published on the platform.

The easiest way is to use [`scdata`](https://github.com/fablabbcn/smartcitizen-data/), the library that we use in Flows. It loads the data of your devices from the API, processes it, and exports the results:

1. [Set up a development environment](https://docs.smartcitizen.me/guides/data/advanced-data-tools.md#development-instructions-advanced) and install `scdata` (`pip install scdata`).
2. Follow the [examples](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples): for instance, [loading and exporting the data of a device](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/scripts/get_device_data.py), or the [processing data notebook](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/04_processing_data.ipynb).
3. To run it periodically, schedule it on your computer (e.g. with `cron`).

When you load a device, `scdata` picks the same blueprint we use for it, from its hardware, and fills it with its sensors and calibration data:

```
import scdata as sc

device = sc.Device(params=sc.APIParams(id=<device-id>))                         # its process blueprint
device = sc.Device(params=sc.APIParams(id=<device-id>), blueprint_kind='long')  # its long one, if it has one
```

`device.blueprint` and `device.blueprint_kind` tell you which one it uses. A device without a hardware (or without a blueprint of the kind you ask for) still loads all its sensors, but has nothing to process. To process a device with another blueprint, use `device.use_blueprint(<name>, <blueprint>)`, which fills it with the sensors of the hardware too. You can also add channels, as explained below.

Of course, you can use any other tool: the data of your devices is available in our [API](https://api.smartcitizen.me), and can also be [downloaded as CSV](https://docs.smartcitizen.me/guides/getting-started/downloading-data.md) from the platform.

### Defining custom functions

With `scdata`, you can add channels to a device with `device.add_channel()`, using the processing functions of `scdata` (in the [`scdata.device.process`](https://github.com/fablabbcn/smartcitizen-data/tree/master/scdata/device/process) module), or your own functions. A channel can use a function from any module (`module` in the channel definition), including one defined in your own script or notebook. Functions get the device data and the `kwargs` of the channel, and return a `ProcessResult`:

```
from scdata.device.process.error_codes import ProcessResult, StatusCode

def dew_point(dataframe, **kwargs):
    ''' Dew point (Magnus formula) from a temperature and a humidity column '''
    import numpy as np
    temperature, humidity = dataframe[kwargs['temperature']], dataframe[kwargs['humidity']]
    gamma = np.log(humidity / 100) + 17.62 * temperature / (243.12 + temperature)
    return ProcessResult(243.12 * gamma / (17.62 - gamma), StatusCode.SUCCESS)

device.add_channel({
    'name': 'DEW_POINT',
    'module': '__main__',
    'function': 'dew_point',
    'unit': 'degC',
    'kwargs': {'temperature': 'TEMP', 'humidity': 'HUM'},
})
device.process(channels_list=['DEW_POINT'])
```

Check the [processing data notebook](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/04_processing_data.ipynb) for more examples. New functions are welcome as [pull requests](https://github.com/fablabbcn/smartcitizen-data/pulls) to `scdata`.
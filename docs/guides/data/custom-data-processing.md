# Custom data processing

Some units require performing data processing after readings are collected, and we provide default algorithms for all the data we collect. Iin the default scenario, for those sensors that need it (i.e. electrochemical sensors), _raw data_ is processed outside of the units in a periodic way by [`scdata`](https://github.com/fablabbcn/smartcitizen-data/). However, you might need to perform _custom_ data processing algorithms on your data. You can do so by simply accessing the data on our [API](https://api.smartcitizen.me/), and then working with it _offline_, or you can set up an automatic data processing workflow. To summarise, there are two ways to have a custom data processing:

1. [Set up a development environment](/Guides/data/Install the framework/#development-instructions-advanced) and following the example on [data processing](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples)
2. Follow the guide below for automatic processing

!!!info "Too confusing?"
    [Contact us](mailto:support@smartcitizen.me) and or open a topic in the [forum](https://forum.smartcitizen.me) and we will try to help!

## Automatic data processing

Data is processed in a recurrent manner whenever there is `postprocessing` field in the device data tree. You can check it by visiting `https://api.smartcitizen.me/v0/devices/<device-id>` where `<device-id>` is the number that follows in the url `https://smartcitizen.me/kits/XXXXXX`.

!!! info "How to do it?"
    Visit [these instructions](/Guides/data/Handling calibration data/) to make sure your `postprocessing` is safely stored.

The `postprocessing` field is composed of several subfields being the most important  one for the automatic data processing the `hardware_url`.

The `hardware_url` should point to a valid json file that contains the necessary information for the data processing. This json file is customisable, but should contain at least the fields defined in [the calibration guide](/Guides/data/Handling calibration data/#advanced-setup). In order to customize how our data is processed, we will need to modify the `blueprint_url` and, if we have specific calibration needs, the `versions` field. Once these changes are done, this hardware json should go in the [hardware folder](https://github.com/fablabbcn/smartcitizen-data/tree/master/hardware) or any other place that can host it.

The `blueprint_url` should point to a json that defines which postprocessing you want to apply for each channel, which functions and parameters it has, and how the new channels are called (don't worry, there are a lot of examples in the [blueprints folder](https://github.com/fablabbcn/smartcitizen-data/tree/master/blueprints)). In order for your data to be processed automatically, you will need to provide that blueprint to `scdata`. For this, you can host it somewhere, or you can simply make a _pull request_ to the [scdata github repository](https://github.com/fablabbcn/smartcitizen-data), having the new json in the `blueprints` folder. Finally, you will then need to modify `hardware` json and update the blueprint field of your kit, with the new `blueprint_url`. See [below](/Guides/data/Custom data processing/#defining-custom-functions) to understand how this blueprint works and how to write custom fuctions.

In case your kit has specific calibration data needs, you will also need to modify the `versions` field. This field is a list which contains the history of the kit in terms of calibration (calibrations can change with time):

```
    {
      "ids": {
        "AS_48_32": "132070362",
        "AS_49_10": "212070552",
        "PT_49_23": "12-000445"
      },
      "from": "2021-01-21",
      "to": null
    }
```

Each of the `ids` field make reference to specific calibration ids for each timespan, where the `from` and `to` fields are the dates during which those ids where valid. This method ensures allows to change sensors with time, and also considers that normally sensors that have specific calibrations use a serial number or similar to identify them.

In the `ids` field, the keys (`AS_48_32`, `AS_49_10`, ... in the example above), define the type of sensor id (`AS` is an Alphasense sensor, `PT` is a PT100 temperature probe) and potentially other useful identifiers, such ADC addresses and channels (i.e. `AS_48_32` defines an Alphasense sensor connected to the ADC in address 0x48 and channel 3 for the _working electrode_ and channel 2 for the _auxiliary electrode_). Other sensor types would need to defined and we can support in the implementation process. Finally, the actual sensor id, and the calibration data associated with it, is stored in _another_ json, this time in [the calibrations folder](https://github.com/fablabbcn/smartcitizen-data/tree/master/calibrations). Similarly to the blueprints above, a simple _pull request_ would work.

### Defining custom functions

If you want to define custom processing functions, make a Pull Request to [the repository of scdata](https://github.com/fablabbcn/smartcitizen-data/pulls) to integrate your functions. Otherwise, you can make a fork and install the package in `editable mode`. You can then add the functions in the [device processing](https://github.com/fablabbcn/smartcitizen-data/tree/master/scdata/device/process) folder of your own. We are available at [support@smartcitizen.me](mailto:support@smartcitizen.me) for more support.


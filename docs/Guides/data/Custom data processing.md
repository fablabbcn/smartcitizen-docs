# Custom data processing

!!! warning "WIP"
    This is a WIP. More info coming **very** soon.

Data is processed outside of the sensors in a periodic way by [`scdata`](https://github.com/fablabbcn/smartcitizen-data/). There are three ways to have a custom data processing:

1. [Contact us](mailto:support@smartcitizen.me) and request it
2. [Set up a development environment](/Guides/data/Install the framework/) and following the example on [data processing](https://github.com/fablabbcn/smartcitizen-data/examples/README.md)
3. Follow the guide below for automatic processing

## Automatic data processing

Data is processed in a recurrent manner whenever there is `postprocessing` in the device. You can check it by visiting `https://api.smartcitizen.me/v0/devices/<device-id>` where `<device-id>` is the number that follows in the url `https://smartcitizen.me/kits/XXXXXX`.

!!! info "How to do it?"
    Visit [these instructions](/Guides/data/Handling calibration data/) to make sure your `postprocessing` is safely stored.

The `postprocessing` is comprised of several fields as defined in the guide above. In order to have custom postprocessing workflows, you need to modify the `blueprint_url` and _maybe_, the hardware url. The `blueprint_url` should point to a valid `json` file following the structure shown in the [examples folder in the `scdata` repository](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples/notebooks). Inside this blueprint, `metrics` can be added to be generated according to the `device`'s available sensors.

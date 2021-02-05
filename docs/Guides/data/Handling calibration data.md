# Handling calibration data

The calibration data for is managed by an unique hardware ID, and should be visible in the device itself (on a sticker, normally on the form of `SCXSXX000X`). This ID serves to identify the hardware calibration data, alongside with the processing description we want for that device. All this information can be saved in the platform's device using the `postprocessing` field of the device.

## How to store data

The easiest way is to go to the kit-edit view of your kit: https://smartcitizen.me/kits/XXXXX/edit

![](/assets/images/postprocessing_edit.png)

In there, you can update the fields for `blueprint` and `hardware`:

- `hardware_url`: this field defines an url for hardware calibration IDs to be loaded from. It virtually can load a **valid json** from any url, as long as it follows the instructions defined [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/hardware/README.md). The default hardware definitions are in the [scdata github repository](https://github.com/fablabbcn/smartcitizen-data/tree/master/hardware) and can be identified per ID. You can just take the corresponding ID and click in the `raw` button to get the url needed. This field should look something like: `https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/hardware/SCAS21001.json`
- `blueprint_url`: this field defines the post-processing to be done in the form of a `device-blueprint`. It virtually can load a valid json from any url, as long as it follows the instructions defined [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/01_getting_started.ipynb) and [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/04_processing_data.ipynb). If you want to use the base processing select it from the [blueprints folder](https://github.com/fablabbcn/smartcitizen-data/tree/master/blueprints), only selecting the `raw` json as mentioned above. If you have doubts, please, [contact us](mailto:support@smartcitizen.me) to make sure. Finally, other blueprints can be added as defined [in this guide](/Guides/data/Custom%20data%20processing/)

### Alternative method

Alternatively, in order to post this data, you can follow to other methods:

- either send us the kit ID and it's corresponding hardware ID, and we will do this for you
- or, if you are familiar with `http requests` you can `post` this data as such:

```
curl 'https://api.smartcitizen.me/v0/devices/<DEVICE-ID>' -X PATCH -H 'Authorization: Bearer <BEARER-FROM-YOUR-USER-PROFILE>' -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"postprocessing_attributes": {"blueprint_url": "https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/blueprints/<BLUEPRINT_ID>.json", "hardware_url": "https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/hardware/<HARDWARE_ID>.json"}}' --compressed
```

You can get your authorization token on your user profile page in the OAuth section. Make sure to change the following fields in the command above:

- `<DEVICE-ID>`
- `<BEARER-FROM-YOUR-USER-PROFILE>`
- `<HARDWARE_ID>`, for instance `SCAS210002`
- `<BLUEPRINT_ID>`, for instance `sc_21_station_module` for Smart Citizen Stations

!!! info "Check it out"
    Once this process is done, you should be able to check that the `postprocessing` is safely stored in the Platform by visiting: `https://api.smartcitizen.me/v0/devices/<DEVICE-ID>/`. After this, we will take care of processing the data in a periodic way.
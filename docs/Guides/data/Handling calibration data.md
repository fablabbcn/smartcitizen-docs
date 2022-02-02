# Handling calibration data

## How to store data

The calibration data for is managed by a unique `hardware ID`, and should be visible on the device itself (on a yellow sticker, normally on the form of <span style="color: black; background: orange;border-radius: 35px;padding:0 7px;border: solid 1px #C7BEB6;font-weight: bold;">SCAS21000X</span>) as seen below:

![](/assets/images/postprocessing_id.jpg)

!!! danger
    This `hardware ID` is not the same as the `kit ID`. The `kit ID` is the number you have after the [smartcitizen.me/kits/](https://smartcitizen.me/kits/) url where you see the data of your kit. The `hardware ID` is the one in the sticker. The hardware ID is meant to never change, while the `kit ID` can change as you can register your kit many times!

The easiest way to store this ID is to visit your kit and click on the **EDIT** button:

![](/assets/images/postprocessing_edit_click.png)

Then, in `hardware URL` field, introduce the number in the yellow sticker. Save your work and you are done!

![](/assets/images/postprocessing_edit.png)


## Advanced setup

!!! warning
    Only follow these steps if you are working on the data post-processing of the sensors, or you know what all this means!

This ID serves to identify the hardware calibration data, alongside with the processing description we want for that device. All this information can be saved in the platform's device using the `postprocessing` field of the device.

The `hardware url` field in the kit edit page can contain a simple `id` as shown above or an URL pointing to a valid `json`:

![](/assets/images/postprocessing_edit_url.png)

This url should point to a **valid json**, and as long as it follows the instructions defined [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/hardware/README.md), it will be picked up for data postprocessing. A simpler way, is that it can simply be one of the `HARDWARE-ID` from the list of jsons available in `https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/hardware/<HARDWARE-ID>.json`. The default hardware definitions are in the [scdata github repository](https://github.com/fablabbcn/smartcitizen-data/tree/master/hardware) and can be found per `ID.json`. You can just take the corresponding ID and click in the `raw` button to get the url needed. If you are using this method, and an url from github, this field should look something like: `https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/hardware/SCAS21001.json`.

With either method, url or `HARDWARE-ID`, the json file needs to follow the instructions below to successfully be a valid postprocessing:

```
{
  "blueprint_url": "https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/blueprints/sck_21.json",
  "description": "Smart Citizen Kit 2.1 With PMS5003",
  "versions": [],
  "forwarding": "nilu"
}
```

- `blueprint_url`: this field defines the post-processing to be done in the form of a `device-blueprint`. It virtually can load a valid json from any url, as long as it follows the instructions defined [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/01_getting_started.ipynb) and [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/04_processing_data.ipynb). If you want to use the base processing select it from the [blueprints folder](https://github.com/fablabbcn/smartcitizen-data/tree/master/blueprints), only selecting the `raw` json as mentioned above. If you have doubts, please, [contact us](mailto:support@smartcitizen.me) to make sure everything will run smoothly. Finally, other blueprints can be added as defined [in this guide](/Guides/data/Custom%20data%20processing/)
- `description`: brief description of the hardware
- `versions`: list containing hardware versions (in case sensors where replaced, but kept in the same physical unit).
    ```
      "versions": [
        {
          "ids": {
            "AS_48_01": "162581715",
            "AS_48_23": "202365014",
            "AS_4A_01": "164200218",
            "AS_4A_23": "204440527"
          },
          "from": "2020-11-30",
          "to": null
        }
      ]
    ```
- `forwarding`: if this device needs to be forwarded to another data platform. Current supported platforms are specified in [the connectors](https://github.com/fablabbcn/smartcitizen-data/tree/master/connectors) folder

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

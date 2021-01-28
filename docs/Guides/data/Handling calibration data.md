# Handling calibration data

The calibration data for is managed by an unique hardware ID, and should be visible in the device itself (on a sticker, normally on the form of `SCXSXX000X`). This ID can be saved in the platform's device using the `postprocessing_info` field by a `http` request. We are working on an implementation to have this in the kit edit view in [smartcitizen.me](https://smartcitize.me), but it's currently not available. Therefore, in order to link this data, you can:
- either send us the kit ID and it's corresponding hardware ID, and we will do this for you
- or, if you are familiar with `http requests` you can `post` this data as such:

```
curl 'https://api.smartcitizen.me/v0/devices/<DEVICE-ID>' -X PATCH -H 'Authorization: Bearer <BEARER-FROM-YOUR-USER-PROFILE>' -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"postprocessing_info": {"updated_at": "<DATE IN UTC - FORMAT YYYY-mm-DDTHH:MM:SS>", "blueprint_url": "https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/blueprints/sc_21_station_module.json", "hardware_url": "https://raw.githubusercontent.com/fablabbcn/smartcitizen-data/master/hardware/<HARDWARE_ID>.json", "latest_postprocessing": "null"}}' --compressed
```

You can get your authorization token on your user profile page in the OAuth section. Make sure to change the following fields in the command above:

- `<DEVICE-ID>`
- `<BEARER-FROM-YOUR-USER-PROFILE>`
- `<DATE IN UTC - FORMAT YYYY-mm-DDTHH:MM:SS>`, for instance `2021-01-14T13:09:23Z`
- `<HARDWARE_ID>`, for instance `SCAS210002`

Once this process is done, you should be able to check that the `postprocessing_info` is safely stored in the Platform by visiting: `https://api.smartcitizen.me/v0/devices/<DEVICE-ID>/`. After this, we will take care of processing the data in a periodic way.

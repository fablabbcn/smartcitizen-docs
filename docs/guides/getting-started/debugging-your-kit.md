# Debugging your kit

<img src="https://live.staticflickr.com/65535/50977039386_c250d3141d_k.jpg" width="2000" height="1333" alt="Smart Citizen Kits being tested at Fab Lab Barcelona">

This guide will try to summarize the basic steps to debug your kits whenever there's any problem. Let's be clear, there is no unique reason or point of failure for the kits to fail, and very likely, if you use them extensively, something will happen, either after 1 month, 1 year, or 5 years. It is key to know how to debug them:

1. Reset the kit using the **hardware reset button**. This is either here:

    ![](/assets/images/sck_2/SCK21_Reset.png)

    or here:

    ![](/assets/images/station-v3-bottom-anotated-reset.jpeg)

    or here (similar 3D printed versions will also have a small hole):

    ![](/assets/images/station-small-reset.jpeg)

    or here:

    ![](/assets/images/reset_water.jpg)

2. If this doesn't solve the problem, you might want to connect to the kits [using the Shell](/guides/getting-started/using-the-shell/).

3. The next steps would depend on what the actual problem of your kits is. The most common problems are:
    - Sensor or hardware issues
    - Connectivity or configuration issues

!!! info "Basic steps"
    1. Reset the kit
    2. Follow this guide
    3. Check the [FAQs](/_FAQ)
    4. Check the [forum]({{ extra.urls.forum.link }})
    5. Ask [support]({{ extra.urls.support.link }}) with a nice explanation

## Sensors or hardware issues

As said above, there is no single point of failure for the kits.

1. If the LED is working normally, but there is one or more sensosr that are not responding, connect the [Shell](/guides/getting-started/using-the-shell/) and type:

```
version
```

Note this for later. If it's an old version of the firmware, it might help to [directly upgrade](/Guides/firmware/Update the firmware/).

```
sensor
```

This should show if all the sensors are being recognised. If one of them is missing from the list, you can try to check the `i2c` bus (where most of the sensors are connected):

```
i2c
```

If one of the sensors is not shown, it means that there is probably a hardware issue with the sensor itself and that the microcontroller is not recognising it. Now, it would be useful to look for [corrosion signs](https://forum.smartcitizen.me/t/unit-failure-suffering-from-weather/1262) around the sensors and maybe reflash the firmware in case there is a better detection of the sensors in a firmware update. Otherwise, it is likely that the hardware is no longer functioning and it needs replacement.

2. If the [LED is static](https://forum.smartcitizen.me/t/persistent-green-light-during-onboarding/1330/25), very likely there is a problem with the detection or an electric problem with the sensors. For this, it is useful to start disconnecting each component to understand which component fails:

- Disconnect the power (USB and battery) and disconnect the PMS5003 sensor. Power on again and check
- Disconnect the power (USB and battery) and disconnect the Urban Board. Power on again and check

If this doesn't help, try to [reflash the firmware](/Guides/firmware/Update the firmware/), as there might be improvements. If it helps, also update and check if it improves. If the sensors heat up too much (it burns to touch), there might be an electric issue.

## Connectivity or configuration issues

Normally, configuration or connectivity issues can be due to the following reasons:

- Typo during the setup process
- Old firmware

1. If **not** using the [Shell](/guides/getting-started/using-the-shell/), make sure that the information provided for the network is correct by putting the SCK in SETUP mode (RED LED) and accessing the SmartCitizeXXXX network.

    ![](/assets/images/sck_2/esp_force_upload_1.png)

2. If using the [Shell](/guides/getting-started/using-the-shell/), you can check the recording configuration by typing:

    ```
    config
    ```

    If you see a problem with the configuration, you can fix each item or the whole thing by typing:

    ```
    config -mode network -wifi "SSID" "PASS" -token token
    ```

    !!! danger "Beware of the quoutes"
        Note that the `token` **does not have quotes** around it and that the `SSID` and `PASS` have **straight** quotes.

3. If the issue is not solved, you can use the [Shell](/guides/getting-started/using-the-shell/) and look for an `ERROR` message. You can write in the [forum]({{ extra.urls.forum.link }}) and we will support there!

!!! info "Not solved"?
    In case there is no problem with the configuration, there problem might get solved by a firmware update.

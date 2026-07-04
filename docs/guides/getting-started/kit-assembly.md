# Assembling a Smart Citizen Kit

This guide you throught the assembly process of the Smart Citizen Kits, register them, and deploy them to start collecting data.


!!! info ""
    Depending on what type of device you have, you will need to start at a different step:

    * If you have a DIY SCK, you will need to follow the [device assembly section](#device-assembly) and then move on to the [device registration section](#device-registration).
    * For cases that requested pre-assembled kits, you can skip ahead to the [device registration section](#device-registration).


!!! warning "Mobile kits and Stations"
    Mobile kits and kits with more complex metrics (CO2, NO2, etc.) are not available as DIY due to their complexity and the need for more elaborate testing before shipment.

    If you have purchased or received these devices, they will have been shipped pre-assembled.

## Device assembly

DIY kits will need to be assembled before deployment. Whether you have purchased or received the components, or if you have manufactured them yourself, make sure you have all the components needed. If you have purchased them, all the neccessary components are shipped along with the sensors, including 3D printed enclosure components, screws, etc.

!!! warning "Tools"
    Simple tools like screw drivers **are not included** and will need to be acquired separately to complete the building process.

### Components

!!! warning "Better use the shell"
    For DIY kits, there is a small code printed on the box (a four-digit code with a mix of letters and numbers - see component photos below). You will need this code to identify your device while registering it. **It is important not to mix up the numbers,** so keep all the components from one box together and keep track of which device corresponds to which device number.

    We suggest you transfer the sticker from the box to the bottom of the PM sensor (see picture below) if there is not already a sticker with the same number. This way, you always have clear which device is which, and this placement gives easy access to check the code when the sensors are deployed.

    <img src="/assets/images/pm-sensor-mac-address.jpg" alt="">

#### Indoor Devices

For **indoor DIY kits**, you will need the following components:

* 1 x "multipurpose" cover[^2] (3D printed)
* 1 x base (3D printed)
* 1 x Smart Citizen Starter Pack box:
  * Smart Citizen Kit 2.3 with PM sensor
  * SD card and reader
  * 2Ah Battery
  * USB charger and cable
* 1 x plastic bag with the following components:
  * 2 x latches
  * 1 x clip for PM and electronics board
  * 6 x M3x30mm INOX screws
  * 2x M3x10mm screws

<div><figure><img src="/assets/images/indoor-diy-components-front.jpg" alt=""><figcaption><p>Indoor DIY components (front)</p></figcaption></figure> <figure><img src="/assets/images/indoor-diy-components-back.jpg" alt=""><figcaption><p>Indoor DIY components (back)</p></figcaption></figure></div>

<figure><img src="/assets/images/electronic-components.jpg" alt=""><figcaption><p>Contents inside of Smart Citizen Kit Starter Pack</p></figcaption></figure>

<figure><img src="/assets/images/screws-clip-components.jpg" alt=""><figcaption><p>Contents inside of components bag</p></figcaption></figure>

#### Outdoor Devices

For **outdoor DIY kits**, you will need the following components:

* 1 x outdoor cover[^3] (3D printed) :warning:
* 1 x base (3D printed)
* 1 x Smart Citizen Starter Pack box:
  * Smart Citizen Kit 2.3 with PM sensor
  * SD card and reader
  * 2Ah Battery
  * USB charger and cable
* 1 x plastic bag with the following components:
  * 2 x latches
  * 1 x clip for PM and electronics board
  * 6 x M3x30mm INOX screws
  * 2 x M3x10mm screws
  * 2 x nylon spacers
* 1 x aluminum umbrella
* 1 x power supply with cables with cover
* 1 x plastic bag with the following components:
  * 4 x M3x15mm screws
  * 1 x M4x10mm screw
  * 1 x M4x25mm screw
  * 4 x M3x15mm screws
* Filtering foam[^4] (large sheet of thin black foam, roughly A4 size)

<div><figure><img src="/assets/images/outdoor-diy-components-front.jpg" alt=""><figcaption><p>Outdoor DIY components (front)</p></figcaption></figure> <figure><img src="/assets/images/outdoor-diy-components-back.jpg" alt=""><figcaption><p>Outdoor DIY components (back)</p></figcaption></figure></div>

<div><figure><img src="/assets/images/outdoor-diy-components-umbrella.jpg" alt=""><figcaption><p>Outdoor DIY components (umbrella)</p></figcaption></figure> <figure><img src="/assets/images/screws-outdoor-components.jpg" alt=""><figcaption><p>Outdoor DIY components (umbrella screws)</p></figcaption></figure></div>

<figure><img src="/assets/images/electronic-components.jpg" alt=""><figcaption><p>Contents inside of Smart Citizen Kit Starter Pack</p></figcaption></figure>

<figure><img src="/assets/images/screws-clip-components.jpg" alt=""><figcaption><p>Contents inside of components bag</p></figcaption></figure>

**Tools (included)**

* 1 x 2.5 HEX key
* 1 x 3 HEX key (for outdoor umbrella only)

**Tools (not included, but needed)**

* 1 x Phillips screw driver

### Assembly Steps

#### 1. Assemble the enclosure

Insert the 6 x M3x30mm INOX screws as indicated in the photographs below.

<div><figure><img src="/assets/images/pre-assembly-enclosure.jpg" alt=""><figcaption><p>Pre-assembly enclosure</p></figcaption></figure> <figure><img src="/assets/images/post-assembly-enclosure.jpg" alt=""><figcaption><p>Post-assembly enclosure</p></figcaption></figure></div>

!!! info ""
    It is easiest to start with the screws on the individual sides of the enclosure, and then to close the box with the hinges in order to align more precisely the two sides.

!!! danger ""
    Do not screw the components too tightly, they just need to be screwed into place so that the head of the screw is touching the 3D printed component.

#### 2. Assemble the device

* Insert the micro SD card into the slot

<div align="left"><figure><img src="/assets/images/insert-sd-card.jpg" alt=""><figcaption></figcaption></figure></div>

* Separate the two boards, insert the nylon spacers, then reconnect the boards assuring that the pins are correctly aligned. (_**See video below.**_)

* Insert the PCB boards into the 3D printed clip. There is a small groove where the board sits, slide the board all the way in and then snap the two other corners into place. (_**See video below.**_)

<div><figure><img src="/assets/images/data-urban-board-assembly.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/data-urban-board-assembly-clip.jpg" alt=""><figcaption></figcaption></figure></div>

<video controls width="100%">
    <source src="/assets/images/clip-guide.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

* Insert the PM sensor into it's slot in the clip, and push it snugly into place

<div><figure><img src="/assets/images/pm-assembly-clip.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/pm-assembly-clip-side.jpg" alt=""><figcaption></figcaption></figure></div>

* Connect the PM cable from the PCB board to the PM sensor feeding it through the holders on the back of the clip to keep it flat. The cable orientation does not matter, both ends are the same.

<div><figure><img src="/assets/images/pm-assembly-clip-top.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/pm-assembly-clip-bottom.jpg" alt=""><figcaption></figcaption></figure></div>

* Insert the components into the base of the enclosure, ensuring that it is fully pushed into the enclosure:

<figure><img src="/assets/images/clip-assembly-enclosure.jpg" alt=""><figcaption></figcaption></figure>

* Tuck the battery into place behind the PCB board, using the PM cable to keep it in place:

<figure><img src="/assets/images/clip-assembly-enclosure-battery.jpg" alt=""><figcaption></figcaption></figure>

* Use the 2x M3x10mm screws and the 2.5 HEX key to screw the clip and components into place:

<figure><img src="/assets/images/clip-assembly-enclosure-battery-screws.jpg" alt=""><figcaption></figcaption></figure>

#### 3. Assemble the umbrella (for outdoor devices only)

* Using the 2.5 HEX key, install the 4 x M3x15mm screws into the four holes on the underside of the umbrella.

<div><figure><img src="/assets/images/umbrella-screws.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/umbrella-components.jpg" alt=""><figcaption></figcaption></figure></div>

!!! danger ""
    These screws should only be screwed in far enough that the screws touch the material below, they do not need to be tightened further, doing so can damage the umbrella.

* Align the enclosure as indicated in the left image below. Using the M4x10mm screw and the 3 HEX key connect the power supply box to the umbrella (bottom left hole, as indicated in the right image), then secure the enclosure using the M4x25mm screw (top left hole) with the 3 HEX key. This should lock the device in place. Check that the device does not move and that you can see the screw pushing the top of the device down securely.

<div><figure><img src="/assets/images/umbrella-kit-power-supply.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/umbrella-kit-power-supply-open.jpg" alt=""><figcaption></figcaption></figure></div>

* Using the 4 x M3x15mm screws and a Phillips screw driver, attach the power supply cover.

<figure><img src="/assets/images/umbrella-kit-power-supply-closed.jpg" alt=""><figcaption></figcaption></figure>

* Feed the USB cable through the enclosure box and plug it into the device.

<div><figure><img src="/assets/images/umbrella-kit-power-supply-cable.jpg" alt=""><figcaption></figcaption></figure> <figure><img src="/assets/images/usb-power.jpg" alt=""><figcaption></figcaption></figure></div>

* Connect the battery and plug in the device into a wall outlet.

<figure><img src="/assets/images/battery.jpg" alt=""><figcaption></figcaption></figure>

!!! warning ""
    Due to the power needs of the SCK2.3 (and SCK2.2), the SCK always needs a battery connected.


* Cut and insert filtering foam to protect the sensors from water and dust buildup (this foam was included with other materials as a large sheet, roughly A4).

!!! info ""
    Note, this is the foam we are talking about...

    <img src="/assets/images/foam.jpg" alt="" data-size="original">

<figure><img src="/assets/images/kit-assembly-final.jpg" alt=""><figcaption></figcaption></figure>

## Device registration

Once the device is assembled, you can proceed to register your device in the [Smart Citizen Platform](https://smartcitizen.me/kits). There are two steps to this:

1. [Create an account in the platform, and register all your devices on it](#onboarding-your-device)
2. Share the account name with Smart Citizen Team ([info@smartcitizen.me](mailto:info@smartcitizen.me)) to enable _research_ options
3. [Enable data forwarding to CitiObs tools if you want to contribute data](#enable-data-forwarding-to-citiobs-platform)

### Onboarding your device

The _onboarding_ app will guide you through the process of the setup using simple language and a friendly graphic language.

!!! danger "To read before you proceed"

    The Smart Citizen platform requires a free account to register a device or, in other words, each device requires an owner.

Visit the _onboarding_ app at [start.smartcitizen.me](https://start.smartcitizen.me/). Before you start make sure you have:

* A computer to visit the onboarding app
* A smartphone (or tablet, or another computer) to connect to the kit and configure it

The app will guide you through the steps. Let us know if there is any issue.

### Enable data forwarding to CitiObs Platform

The easiest way to enable forwarding is to visit your device on the website[^5] and click on the `EDIT button` on the bottom part of the graphs.

![Edit Smart Citizen Kit](/assets/images/edit-kit-link.jpg)

Then, scroll down to the forwarding section and enable the checkbox. Make sure all the other settings are shown as in the image below, and to hit **update** when you are done!

<figure><img src="/assets/images/advanced-options.jpg" alt=""><figcaption><p>Enable MQTT forwarding</p></figcaption></figure>

In addition, please add the `CitiObs` `tag` on your device:

![Add device tags](/assets/images/kit-tags.jpg)

!!! warning ""
    If you do not see this, please contact us at [info@smartcitizen.me](mailto:info@smartcitizen.me)

!!! success ""
    Once you are done, make sure you hit **Update**!

### Enable notifications

The easiest way to enable forwarding is to visit your device on the website[^5] and click on the`EDIT button` on the bottom part of the graphs.

![Edit Smart Citizen Kit](/assets/images/edit-kit-link.jpg)

Then, scroll down to the notifications section and enable both. This will trigger an email in case the device stops publishing. This step is crucial to ensure that, in the event of sensor malfunction, we can avoid data loss. There are no additional notifications on that email.

![Enable notifications](/assets/images/notifications.jpg)

!!! success ""
    Once you are done, make sure you hit **Update**!

### Create an _experiment_

_An experiment is a way to group devices and share data with others through the Smart Citizen Platform. You can create an experiment by visiting your user profile:_

<figure><img src="/assets/images/user-experiment.jpg" alt=""><figcaption></figcaption></figure>

Fill out the relevant information such as `name`, `description`, `start and end dates` and add the devices on the `KITS` section. You can search there for your COs devices and create a collection of devices which is very handy to share later on.

!!! info ""
    You can look at an example experiment at: [https://api.smartcitizen.me/ui/experiments/6](https://api.smartcitizen.me/ui/experiments/6)

### Advanced devices

Advanced devices (such as NO2 devices), requires handling of calibration data. For this reason, it's necessary to store the physical ID (`Station ID` or `Hardware ID`) of the unit alongside to the virtual device in the Smart Citizen Platform. The hardware ID should normally be in a sticker to the enclosure both inside and outside and looks like this:

![Hardware IDs](/assets/images/hardware-id.jpg)

**Station ID**

* This number is important to relate to the actual calibration values of the sensors, stored in the data repository. In order to postprocess the data and calculate pollutants, make sure that the `Station ID` is safely stored in the platform's device

!!! danger ""
    This hardware ID is not the same as the `device ID`. The `device ID` is the number you have after the smartcitizen.me/kits/ url where you see the data of your device. The `Station ID` is the one in the sticker. The `Station ID` is not meant to change, while the `device ID` can change as you can register your kit many times!

* The easiest way to enable forwarding is to visit your device on the website[^5] and click on the`EDIT button` on the bottom part of the graphs.

![Edit Smart Citizen Kit](/assets/images/edit-kit-link.jpg)

* Then, in the `hardware URL` field, introduce the number in the sticker (it should be something like `SCAS2200XX`)

![Postprocessing hardware URL](/assets/images/advanced-options-postprocessing.jpg)

* Once this process is done, you should be able to check that the postprocessing is safely stored in the Platform by visiting the following link (Make sure your`<DEVICE-ID>` is correct): `https://api.smartcitizen.me/v0/devices/<DEVICE-ID>/`

!!! success ""
    After this, we will take care of processing the data in a periodic way.

## Device Deployment

### Indoor devices

There are **only** two possibilities for the device to be placed indoors: laterally or vertically.

!!! danger ""
    The device **should never be placed horizontally** (wide side flat on a surface). This placement would cover completely the sensor inlets, or leave them exposed to dust accumulation. Likewise, the sensors, do not work properly on this configuration.


![Lateral placement of devices](/assets/images/lateral-placement.jpg)
![Vertical placement of devices (note the PM sensor position)](/assets/images/vertical-placement.jpg)

### Outdoor devices

The outdoor devices are deployed as below:

![Outdoor device installation reference](/assets/images/station-small-front.jpg)

Some basic deployment tips:

* Try to keep the device continuously powered if it is installed in a fixed location.
* Avoid using the device in places with high humidity or large amounts of dust; otherwise, clean/check the device periodically to prevent potential issues.
* Avoid covering the sensors, especially the PM sensor.
* Deploy the device facing downwards if outdoors, so that dust doesn't accumulate on the sensors.
* Avoid direct airflow towards the sensors; if exposed under flow conditions, keep the flow parallel to the sensor surfaces.
* Avoid exhaust from air conditioning units, kitchens, etc.
* Protect the sensors from moisture using filtering foam, nail polish, or both to cover the sensor pads (see [here](/_FAQ/#are-the-electronics-waterproof)).

### Battery Information

All devices comes with USB cable and an adapter with an additional 2000mAh LiPo battery. The SCK has a micro USB port and can be charged like any smartphone or tablet using a dedicated adapter or a computer USB port.

!!! info "Battery info"
    Battery characteristics can be found in the following [link](/_FAQ/#what-batteries-are-shipped-with-the-kits)

    :warning: **Remember** - due to the power needs of the SCK2.3 (and SCK2.2), the battery always needs a battery connected.

### Data logging

**Wi-Fi Mode (online)** This is the standard mode and requires a Wi-Fi connection. In this way, the device will publish data every minute (time resolution can be configured) on the smartcitizen.me platform. If a micro SD card is inserted, the data will be stored in duplicate as a backup.

!!! info ""
    The kit supports Wi-Fi WEP, WPA/WPA2 and open networks, those the standard Wi-Fi networks found in domestic and small businesses environments. However, it does not support WPA/WPA2 Enterprise networks such as EDUROAM or networks with captive portals such as those found in Airports and Hotels.

### **SD Mode (offline)**

If we do not have an internet connection, we can use the SD mode. In this case, the device will record the data on the micro SD card. Later we can read the card using a card reader. The recorded data can be visually explored in a spreadsheet but also published on the platform utilising the [UPLOAD CSV](guides/getting-started/uploading-sd-card-data/) option.

### **Limitations**

!!! danger ""
    While on SD-card mode, the device needs constant power (either USB or battery).


* The Kit location needs to be set during the installation process, and it can be updated at any time using the `EDIT` option on the platform if you made a mistake. However, the Kit does not record its location automatically neither we can't have multiple locations for the same Kit in the platform.
* **Unstable Wi-Fi environments need careful consideration**. Check these [guidelines for support](/_FAQ/#what-can-i-do-in-unstable-wi-fi-environments).


## Notes

[^1]: do-it-yourself (or in other words, not assembled)
[^2]: This cover is different from the outdoor one below. It has some slots for passing zip ties and a small indentation for hanging the kit on a wall with a screw.
[^3]: This cover is different from the indoor one above. It has two support holes for screws and two notches for the lower screws of the umbrella.
[^4]: This is **not** the foam that comes inside of each individual Smart Citizen Kit box.
[^5]: [https://smartcitizen.me/kits/DEVICE-ID](https://smartcitizen.me/kits/%3CDEVICE-ID%3E)
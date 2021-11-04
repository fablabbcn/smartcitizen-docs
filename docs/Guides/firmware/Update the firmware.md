When new features are developed or bugs are fixed we will release new versions of the SCK firmware.

## Make a back-up of your info

!!! info
	If you already configured your kit on the smartcitizen platform **you will need the token that the platform gave you during the onboarding process**, to recover it from your kit:

	1. **Click your kit button** until the kit is in [setup mode](../../../../Smart%20Citizen%20Kit/#setup-mode), the led should be red.
	2. **Connect to the kit** with your mobile device as you did during the onboarding process.

	3. **Write down the token** of your kit.

	![](/assets/images/sck_2/ap_token.png)

	After updating the firmware follow this same steps to input the token and wifi credentials, after this your kit will be publishing on the same registered device than before.

!!! info "A note about versions"
	:white_check_mark: The guide below applies to both, SCK 2.0 and SCK2.1.

## Updating the SAM firmware

The SAMD21 (SAM for short) chip manages the main part of the firmware. This firmware is frequently updated with latest improvements in the official [firmware repository](https://github.com/fablabbcn/smartcitizen-kit-21/tree/master/sam). Check the [releases pages](https://github.com/fablabbcn/smartcitizen-kit-21/releases) for more info.

!!! example "Updating your kit is very simple"

	* **Connect your kit** with a micro USB cable to your computer

	* **Double click the reset button** of your SCK, the SCK led should turn green and a new drive called _SCK-20_ should appear on your computer file browser

	![](/assets/images/sck_2/SCK21_Reset.png)

	* Inside the _SCK-20_ drive you should see some files, **double click the _INDEX.HTM_** file and our  [github releases page](https://github.com/fablabbcn/smartcitizen-kit-21/releases/latest) will open in your browser 
	**Download the new firmware** called _SAM_firmware_XXX.uf2_ and save it to your computer

	![](/assets/images/sck_2/uf2_index.png)

	!!! tip
		You can backup your current firmware version just saving the file called _CURRENT.UF2_.

	* Simply **drag the firmware file you downloaded over the _SCK-20_ drive**, your kit led will blink in green and after some seconds it will reset and start with the new version.

	![](/assets/images/sck_2/uf2_drag.png)

## Updating the ESP firmware

The ESP8266 (ESP for short) chip sometimes also needs upgrade to match the lattest version of the SAM firmware. The ESP chip manages all the communications of the SCK with the outer world. The firmware can be found [here](https://github.com/fablabbcn/smartcitizen-kit-21/tree/master/esp).

!!! example	

	*  If your **WiFi module needs a firmware update** when you connect to your kit to setup the network you will see a screen that will ask for the new file. You can find it in our [github releases page](https://github.com/fablabbcn/smartcitizen-kit-21/releases/latest), look for the file called `ESP_firmware_XXX.bin`. If you don't see it, check in a [previous release](https://github.com/fablabbcn/smartcitizen-kit-21/releases) (some releases don't include Wi-Fi firmware)

	* This file needs to be downloaded to the same device (phone or laptop) that is connecting to the _SmartCitizen[...]_ network. If you are using your phone, you will need to download it there

	* Once you have it, you can select the file in the screen below. If it doesn't appear, check the section to [force ESP upload](#force-esp-upload) below

	![](/assets/images/sck_2/esp_update.png)	

	* After the update you just did, you can configure your kit as a new device following the [onboarding](https://start.smartcitizen.me) process or use your previous token as explained before

### Force ESP upload

If you want to force the ESP to upload, please, follow the steps below.

!!! example "Force ESP upload"

	If you already have the latest version but for some reason you still want to upload the firmware, you can **force by clicking the info button** (top right) on the setup screen that you find when conected to your kit in setup mode:

	![](/assets/images/sck_2/esp_force_upload_1.png)

	And activate the _Force allow firmware update_:

	![](/assets/images/sck_2/esp_force_upload_2.png)

	So you will be asked for the firmware file:

	![](/assets/images/sck_2/esp_force_upload_3.png)
	
!!! danger "Doesn't work?"
	Sometimes in the phone the firmware selection screen will not pop up. You can always try to do the _developer-way_ with [check this guide here](/Guides/firmware/Edit the Firmware/#manual-update)

## Using command-line tools

The steps below are a summary of the steps you will need to update the firmware in case you are handling a lot of sensosr. The process builds on top the tools used in the [edit the firmware](/Guides/firmware/Edit%20the%20Firmware), but simplified as we do not want to compile the firmware (since we are not changing it):

1. Install python as per the instructions [here](/Guides/firmware/Edit%20the%20Firmware/#installing-python)

2. Install [python requirements](/Guides/firmware/Edit%20the%20Firmware/#installing-requirements)

3. Install git following [these instructions ](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Check that you need to install it first by simply typing `git` in your terminal. If the output is not `command not found`, skip to step 4

4. In your terminal, navigate to a folder in which you want to download the firmware in. Then, get the firmware following the [instructions here](/Guides/firmware/Edit%20the%20Firmware/#getting-the-firmware_1)

5. Navigate to the firmware folder, plug the sensor to your computer and run the command below.

	This will upload the SAM firmware:
	```
	python make.py flash sam -v
	``` 

	This will also upload the ESP firmware:
	```
	python make.py flash esp -v
	```

	You can upload both at the same time by:
	```
	python make.py flash sam esp -v
	```

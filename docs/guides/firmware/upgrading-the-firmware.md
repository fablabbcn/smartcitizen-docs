# Upgrade the firmware

When new features are developed or bugs are fixed we will release new versions of the SCK firmware.

## Make a back-up of your info

!!! info
	If you already configured your kit on the smartcitizen platform **you will need the token that the platform gave you during the onboarding process**, to recover it from your kit:

	1. **Click your kit button** until the kit is in [setup mode](/hardware/kit/features/#setup-mode/), the led should be red.
	2. **Connect to the kit** with your mobile device as you did during the onboarding process.

	3. **Write down the token** of your kit.

	![](/assets/images/token-input.png)

	After updating the firmware follow this same steps to input the token and wifi credentials, after this your kit will be publishing on the same registered device than before.

!!! info "A note about versions"
	:white_check_mark: The guide below applies to all SCK2.* versions.

!!! danger "If you are updating to `0.9.10`"
	:warning: If you are updating to `0.9.10` we recommend you update first the [ESP](#updating-the-esp-firmware) and later on the [SAM](#updating-the-sam-firmware).

## Updating the SAM firmware

The SAMD21 (SAM for short) chip manages the main part of the firmware. This firmware is frequently updated with latest improvements in the official [firmware repository]({{ extra.urls.firmware.link }}/tree/master/sam). Check the [releases pages]({{ extra.urls.firmware.link }}/releases) for more info.

!!! example "Updating your kit is very simple"

	* **Connect your kit** with a micro USB cable to your computer

	* **Double click the reset button** of your SCK, the SCK led should turn green and a new drive called _SCK-20_ should appear on your computer file browser

	![](/assets/images/sck23-reset-button-with-line.jpg)

	* Inside the _SCK-20_ drive you should see some files, **double click the _INDEX.HTM_** file and our  [github releases page]({{ extra.urls.firmware.link }}/releases/latest) will open in your browser
	**Download the new firmware** called _SAM_firmware_XXX.uf2_ and save it to your computer

	![](/assets/images/uf2-index.png)

	!!! tip
		You can backup your current firmware version just saving the file called _CURRENT.UF2_.

	* Simply **drag the firmware file you downloaded over the _SCK-20_ drive**, your kit led will blink in green and after some seconds it will reset and start with the new version.

	![](/assets/images/uf2-drag.png)

## Updating the ESP firmware

The ESP8266 (ESP for short) chip sometimes also needs upgrade to match the latest version of the SAM firmware. The ESP chip manages all the communications of the SCK with the outer world. The firmware can be found [here]({{ extra.urls.firmware.link }}/tree/master/esp).

!!! example

	*  If your **WiFi module needs a firmware update** when you connect to your kit to setup the network you will see a screen that will ask for the new file. You can find it in our [github releases page]({{ extra.urls.firmware.link }}/releases/latest), look for the file called `ESP_firmware_XXX.bin`. If you don't see it, check in a [previous release]({{ extra.urls.firmware.link }}/releases) (some releases don't include Wi-Fi firmware)

	* This file needs to be downloaded to the same device (phone or laptop) that is connecting to the _SmartCitizen[...]_ network. If you are using your phone, you will need to download it there

	* Once you have it, you can select the file in the screen below. If it doesn't appear, check the section to [force ESP upload](#force-esp-upload) below

	![](/assets/images/sck_2/esp_update.png)

	* After the update you just did, you can configure your kit as a new device following the [onboarding]({{ extra.urls.installation.link }}) process or use your previous token as explained before.

### Force ESP upload

If you want to force the ESP to upload, please, follow the steps below.

!!! example "Force ESP upload"

	If you already have the latest version but for some reason you still want to upload the firmware, you can **force by clicking the info button** (top right) on the setup screen that you find when conected to your kit in setup mode:

	![](/assets/images/esp-force-upload-1.png)

	And activate the _Force allow firmware update_:

	![](/assets/images/esp-force-upload-2.png)

	So you will be asked for the firmware file:

	![](/assets/images/esp-force-upload-3.png)

!!! warning "Make sure to disconnect your data"
	Modern phones will have Wi-Fi and LTE (data) active at the same time. The `SmartCitizen[...]` network doesn't have internet access, so your phone will likely switch to using your data plan. If this happens, make sure to switch it off temporarily while updating the firmware.

!!! danger "Doesn't work?"
	Sometimes in the phone, the firmware selection screen will work when you click on `Browse`. This is very likely because the browser on your phone doesn't have this feature. We recommend using a modern browser (firefox, chrome...) instead of the default Wi-Fi login portal that typically pops up in some phones. 
 	
 	You can always try to do the _developer-way_ with [check this guide here](#using-command-line-tools)

## Using command-line tools

The steps below are a summary of the steps you will need to update the firmware in case you are handling a lot of sensosr. The process builds on top the tools used in the [edit the firmware](/guides/firmware/edit-the-firmware/), but simplified as we do not want to compile the firmware (since we are not changing it):

1. Install `python` (3.*)

2. Clone or download the firmware repository. If you are familiar with `git`, clone the [firmware repository](https://github.com/fablabbcn/smartcitizen-kit-2x) (recursing submodules). You can avoid this by downloading the firmware from GitHub and, in the tools folder, downloading the [tools repository](https://github.com/fablabbcn/smartcitizen-tools) and putting its content in the `tools` folder in the firmware directory

3. Install [requirements](https://github.com/fablabbcn/smartcitizen-tools/blob/master/requirements.txt)

4. Navigate to the firmware folder, plug the SCK to your computer and run the command below. The [SAM firmware has different versions](https://forum.smartcitizen.me/t/wq-sensors-wouldnt-enable/1958/3), defined by `environments`. The `environments` are: `sck2`, `sck21_air`, `sck22_air`, `sck23_air` and `sck_water`. Make rue to use the corresponding one after the `--env` option below. Note that `ESP` doesn't need a flag, as it's independent.

	This will upload the SAM firmware, version `2.3`:
	```
	python make.py flash sam -v --env sck23_air
	```

	This will also upload the ESP firmware:
	```
	python make.py flash esp -v
	```

	You can upload both at the same time by:
	```
	python make.py flash sam esp -v --env sck23_air
	```

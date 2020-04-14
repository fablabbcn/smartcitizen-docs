When new features are developed or bugs are fixed we will release new versions of the SCK firmware.

!!! info
	If you already configured your kit on the smartcitizen platform **you will need the token that the platform gave you during the onboarding process**, to recover it from your kit:

	1. **Click your kit button** until the kit is in [setup mode](../../../../Smart%20Citizen%20Kit/#setup-mode), the led should be red.
	2. **Connecto to the kit** with your mobile device as you did during the onboarding process.
	3. **Write down the token** of your kit.

	![](/assets/images/sck_2/ap_token.png)

	After updating the firmware follow this same steps to input the token and wifi credentials, after this your kit will be publishing on the same registered device than before.

!!! info "A note about versions"
	:white_check_mark: The guide below applies to both, SCK 2.0 and SCK2.1.

!!! example "Updating your kit is very simple"

	* **Connect your kit** with a micro USB cable to your computer.
	* **Double click the reset button** of your SCK, the SCK led should turn green and a new drive called _SCK-20_ should appear on your computer file browser.
	![](/assets/images/sck_2/reset_button.png)
	* Inside the _SCK-20_ drive you should see some files, **double click the _INDEX.HTM_** file and our  [github releases page](https://github.com/fablabbcn/smartcitizen-kit-21/releases/latest) will open in your browser. **Download the new firmware** called _SAM_firmware_XXX.uf2_ and save it to your computer.
	![](/assets/images/sck_2/uf2_index.png)

	!!! tip
		You can backup your current firmware version just saving the file called _CURRENT.UF2_.

	* Simply **drag the firmware file you downloaded over the _SCK-20_ drive**, your kit led will blink in green and after some seconds it will reset and start with the new version.

	![](/assets/images/sck_2/uf2_drag.png)

	*  If your **Wi-Fi module needs a firmware update** when you connect to your kit to setup the network you will see a screen that will ask for the new file. You can find it in our [github releases page](https://github.com/fablabbcn/smartcitizen-kit-21/releases/latest), look for the file called `ESP_firmware_XXX.bin`. If you don't see it, check in a [previous release](https://github.com/fablabbcn/smartcitizen-kit-21/releases) (some releases don't include Wi-Fi firmware).

	![](/assets/images/sck_2/esp_update.png)

	* After the update you just done, you can configure your kit as a new device following the [onboarding](https:start.smartcitizen.me) process or use your previous token as explained before.

!!! tip "Obtain your firmware version remotely (advanced)"
	If you are an advance user managing a big deployment of devices you can obtain remotely the version of all the kits you have registered by looking at the `hardware_info` property of each of your devices using the platform API `/v0/devices/`

	```json
	"hardware_info": {
		"id": "DFD098A750515157382E3120FF101D12",
		"mac": "B6:E6:2D:66:47:6D",
		"time": "2020-04-14T03:00:24Z",
		"esp_bd": "",
		"hw_ver": "2.1",
		"sam_bd": "2019-11-27T12:49:13Z",
		"esp_ver": "",
		"sam_ver": "0.9.6-4e90c77"
	}
	```

	[More info](https://developer.smartcitizen.me/#devices) in the platform API documentation.
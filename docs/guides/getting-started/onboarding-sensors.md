# Onboarding Sensors

The onboarding app guides you through the process of the setup using simple language and a friendly graphic language. It is built as a separate tool from the core Smart Citizen Webpage in order it can be customized for each deployment.

!!! info "Onboarding app"
	Visit the onboarding app at [{{ extra.urls.installation.name }}]({{ extra.urls.installation.link }}). Before you start make sure you have:

	- A computer to visit the onboarding app
	- A smartphone (or tablet, or another computer) to connect to the kit and configure it

The welcome page looks like this:

![](/assets/images/onboarding_1.png)

You can then follow the steps by pressing on _Let's go!_. For experienced users, you can press _Skip instructions_ and go to the _Configuration_ page:

![](/assets/images/onboarding_2.png)

## Connect to the Kit

After this, make sure that the SCK is in [Setup Mode](/hardware/Smart Citizen Kit/#setup-mode) (LED is red) and **connect with your smartphone** to the `SmartCitizen[...]` network.

![](/assets/images/onboarding_3.png)

In your phone, something like below should pop-up:

![](/assets/images/phone-start.png)

!!! danger "If nothing comes up"
	In some cases, your phone will be disconected from the WiFi as it doesn't have access to the internet. Stay connected to it!

	If nothing pop-up in your phone, open your phone's web browser and navigate to sck.me

Now, choose where you want your data to go, either [Wi-Fi Mode](#wi-fi-mode) or [SD-Card Mode](#sd-card-mode)

## Wi-Fi Mode

If you go with Wi-Fi mode, you should see the screen below. In your computer, you should click Next and see a 6 letter token to be input in your phone:

![](/assets/images/token-input.png)

Depending on the mode selected (Wi-Fi or SD card), proceed with the steps and make sure the LED changes color: blue for Wi-Fi, purple for SD card. Once this is done, register your kit and add it to your user profile following the steps:

![](/assets/images/onboarding_4.png)

You can also mark it's location in the map (this doesn't need to be accurate, it's as accurate as you want it to be):

![](/assets/images/onboarding_6.png)

!!! info "Location of the sensor"
	The sensor location is only defined by the user in the registration process. It can be modified afterwards in the _kit edit page_. The Smart Citizen Kit does not retrieve location unless it has an onboard GPS. In this case, **the GPS location never updates the location in the map**.

You can also add some tags to your sensor:

![](/assets/images/onboarding_5.png)

Finally, add the sensor to an **user account** (if you don't have one you can register now). This step is needed as every device needs to be owned by one user:

![](/assets/images/onboarding_7.png)

!!! info "What is the email used for?"
	The user account and email is only used for sensor data emails and sensor notifications (i.e. notification when the battery is almost empty). It is not used for commercial purposes at all, as stated in [our policy](https://smartcitizen.me/policy)

You are done!

![](/assets/images/onboarding_8.png)

!!! info "Working with a community?"
	You can either choose to create a joint email account, or work with each participant with one account. Working with a joint email account speeds things up, but it is not the same sense of ownership. When in doubt, we recommend giving each participant the freedom to choose, and if they do not want to create an account, a fallback option can be used.

## SD-Card Mode

If you go with SD-Card mode, data will be stored **only** on the SD-card. Simply press start and the LED will turn pink:

![](TODO)

## Visit your Kit

Visit the Kit on the platform. **Wait one minute till it publishes data**:

![](/assets/images/onboarding_9.png)

When the data is available, scroll down to make some basic explorations:

![](/assets/images/onboarding_10.png)

!!! info "More on the data"
	The platform allows you to check the data in a basic way, but if you want to have a deeper look you can:

	- [Download the data in CSV](/guides/getting-started/downloading-data/#direct-csv-download)
	- Get it from the [API](/guides/getting-started/downloading-data/#api)
	- Use [python](/data/data-tools/#advanced) to analyse it

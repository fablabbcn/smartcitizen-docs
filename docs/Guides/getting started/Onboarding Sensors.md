Onboarding Sensors
=================

The onboarding app guides you through the process of the setup using simple language and a friendly graphic language. It is built as a separate tool from the core Smart Citizen Webpage in order it can be customized for each deployment.

!!! info "Onboarding app"
	Visit the onboarding app at [start.smartcitizen.me](https://start.smartcitizen.me). Before you start make sure you have:

	- A computer to visit the onboarding app
	- A smartphone (or tablet, or another computer) to connect to the kit and configure it


The welcome page looks like this. For sensors different from the Smart Citizen Kit 2.1, please check the [advanced kit selection](#advanced-kit-selection):

![](/assets/images/onboarding_1.png)

You can then follow the steps by pressing on _Let's go!_. For experienced users, you can press _Skip instructions_ and go to the _Configuration_ page:

![](/assets/images/onboarding_2.png)

After this, make sure that the SCK is in [Setup Mode](/Smart Citizen Kit/#setup-mode) (LED is red) and **connect with your smartphone** to the `SmartCitizen[...]` network.

![](/assets/images/onboarding_3.png)

Depending on the mode selected (Wi-Fi or SD card), proceed with the steps and make sure the LED changes color: blue for Wi-Fi, purple for SD card. Once this is done, register your kit and add it to your user profile following the steps:

![](/assets/images/onboarding_4.png)

You can also mark it's location in the map (this doesn't need to be accurate, it's as accurate as you want it to be):

![](/assets/images/onboarding_6.png)

!!! info "Location of the sensor"
	The sensor location is only defined by the user in the registration process. It can be modified afterwards in the _kit edit page_. The Smart Citizen Kit does not retrieve location unless it has an onboard GPS. In this case, **the GPS location never updates the location in the map**.

You can also add some tags to your sensor:

![](/assets/images/onboarding_5.png)

Finally, add the sensor to your user account (if you don't have one you can register now):

![](/assets/images/onboarding_7.png)

!!! info "What is the email used for?"
	The user account and email is only used for sensor data emails and sensor notifications (i.e. notification when the battery is almost empty). It is not used for commercial purposes at all, as stated in [our policy](https://smartcitizen.me/policy)

You are done!

![](/assets/images/onboarding_8.png)

Visit the Kit on the platform. **Wait one minute till it publishes data**:

![](/assets/images/onboarding_9.png)

When the data is available, scroll down to make some basic explorations:

![](/assets/images/onboarding_10.png)

!!! info "More on the data"
	The platform allows you to check the data in a basic way, but if you want to have a deeper look you can:

	- [Download the data in CSV](/Guides/getting started/Downloading the Data/#download-data)
	- Get it from the [API](/Guides/getting started/Downloading the Data/#api)
	- Use [python](/Data/Data Analysis/) to analyse it

## Advanced Kit Selection

The feature below is for users who want to know how to configure new or customized sensor devices:

!!! example "How to choose a custom kit"

	- Click the 🛠️ icon in the bottom right corner

	![](https://i.imgur.com/Qy7NpXQ.png)

	- Choose the blueprint of the device you want to setup

	![](https://i.imgur.com/ERXdPvK.png)

	- Click save and continue the process as normal

	![](https://i.imgur.com/O6oT13q.png)

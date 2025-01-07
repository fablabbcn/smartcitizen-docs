# Troubleshooting SD-card Mode

This guide will walk you through some easy steps in case your kit is not collecting data on SD-card mode.

## Check if your kit is storing data

1. Plug in your kit with the USB cable provided. A LED on the **blue side** of the kit should light up.

    ![image](/assets/images/sck_2/led_location.png)

2. Check if the LED is...
    + ***Hard flashing pink light*** <span class="led sd-error"></span>. In this case, your kit **IS NOT** storing data.
    + ***Soft fading pink light*** <span class="led sd"></span> with either orange <span class="led sd-chargebat"></span> or green intermitent light <span class="led sd-fullbat"></span>. In this case, your kit **IS** storing data.
    + ***A single green light with less frequency*** <span class="led sd-sleep"></span>. Your kit **IS** storing data.
3. If your kit is **NOT** storing data, you need to follow the steps below using a mobile phone:
    + If you have an iPhone, [follow these steps](#setup-for-iphone)
    + If you have an Android phone, [follow these steps](#setup-for-android)

Below you have a summary of all the possibilities:

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led sd"></span>             | :thumbsup: Collecting data offline              |
| <span class="led sd-warning"></span>    | :warning: Warning. Collecting data but not storing it in sdcard       |
| <span class="led sd-error"></span>       |  ❌ Error. Not collecting data         |
| <span class="led sd-lowbat"></span>      | :battery: Collecting data offline but battery is low, charge the Kit    |
| <span class="led sd-chargebat"></span>   | :battery: Collecting data offline,  battery charging              |
| <span class="led sd-fullbat"></span>     | :battery: Collecting data offline, battery charged          |
| <span class="led sd-sleep"></span>    | :bed: Sleep-mode. Collecting data offline and saving battery               |

## Setup for iPhone

1. Press the **ON/OFF button** on the SCK. The ON/OFF Button is inside the box, next to the USB cable:

    ![image](/assets/images/sck_2/button_location.png)

2. The LED from before should now be **red**.

3. Next, on your iPhone, tap **Settings** > **Wi-Fi**. Your device searches for available Wi-Fi networks and displays them in a list. The kit will appear as `SmartcitizenXXXX`. The last four digits will match the four digit code printed on the kit (on the blue face of the outside, on the gray box inside the box, or both). For example: `SmartcitizenA0D`.

4. Tap the name of the network, then wait for a welcome page to appear.

    !!!warning
        If the captive portal page doesn’t appear or you accidentally closed the page, you can force it to reopen by typing `sck.me` in the any browser search field.


5. Now, you can press on the "Offline mode (SD-Card)" button:

    ![image](/assets/images/sck_2/sd-card-phone-1.png)

6. And then "Start logging" button:

    ![image](/assets/images/sck_2/sd-card-phone-2.png)

7. The LED should be ***Soft fading pink light*** in any of the modes below. Below you have a summary of all the possibilities:

    | LED color                                |  Kit status                                |
    |------------------------------------------|------------------------------------------- |
    | <span class="led sd"></span>             | :thumbsup: Collecting data offline         |
    | <span class="led sd-chargebat"></span>   | :battery: Collecting data offline,  battery charging              |
    | <span class="led sd-fullbat"></span>     | :battery: Collecting data offline, battery charged          |

!!!success
    You are done!

## Setup for Android

1. Press the **ON/OFF button** on the SCK. The ON/OFF Button is inside the box, next to the USB cable:

    ![image](/assets/images/sck_2/button_location.png)

2. The LED from before should now be **red**.

3. Enable Wi-Fi on your Android device. Swipe down from the top of your screen to open the Quick Settings menu. Otherwise, look for the Wi-Fi menu in the phone settings. Your device searches for available Wi-Fi networks and displays them in a list. The kit will appear as `SmartcitizenXXXX`. The last four digits will match the four digit code printed on the kit (on the blue face of the outside, on the gray box inside the box, or both). For example: `SmartcitizenA0D`.

4. Tap the name of the network, then wait for a welcome page to appear.

    !!!warning
        If the captive portal page doesn’t appear or you accidentally closed the page, you can force it to reopen by typing `sck.me` in the any browser search field.

5. Now, you can press on the "Offline mode (SD-Card)" button:

    ![image](/assets/images/sck_2/sd-card-phone-1.png)

6. And then "Start logging" button:

    ![image](/assets/images/sck_2/sd-card-phone-2.png)

7. The LED should be ***Soft fading pink light*** in any of the modes below. Below you have a summary of all the possibilities:

    | LED color                                |  Kit status                                |
    |------------------------------------------|------------------------------------------- |
    | <span class="led sd"></span>             | :thumbsup: Collecting data offline         |
    | <span class="led sd-chargebat"></span>   | :battery: Collecting data offline,  battery charging              |
    | <span class="led sd-fullbat"></span>     | :battery: Collecting data offline, battery charged          |

!!!success
    You are done!

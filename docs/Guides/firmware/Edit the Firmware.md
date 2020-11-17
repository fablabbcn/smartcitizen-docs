The data board of your SmartSmart Citizen Kit is has two **two microcontrollers**:

![](/assets/images/sck_2/SCK21_Microcontrollers.png)

The main one is an **Atmel SAMD21**, this chip is in charge of all the normal tasks like reading the sensors, saving data, interacting with the user, etc. For this chip we need two software components the bootloader and the main firmware.

For communications the SCK has an **ESP8266 microcontroler with Wifi capabilities**, this chip receives instructions from the SAMD21 via serial port and takes care of publishing the collected data through the network and takes care of serving the web pages for the [setup mode](http://docs.smartcitizen.me/Smart%20Citizen%20Kit/#setup-mode) configuration server.


## Development enviroment

The SmartSmart Citizen Kit Firmware is on our [repository on github](https://github.com/fablabbcn/smartcitizen-kit-21) so you will need [git](https://mirrors.edge.kernel.org/pub/software/scm/git/) software [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). To build the SmartSmart Citizen Kit firmware you need a computer with [platformio](https://platformio.org/) installed, you don't need the full IDE installation (Atom). You can follow [this instructions](http://docs.platformio.org/en/latest/installation.html#super-quick-mac-linux) to install only the console version.

For bootloader upload you also need [OpenOCD](http://openocd.org/) somewhere in your PATH. 


## Getting the firmware

To get the firmware just run:

```bash
git clone --recursive https://github.com/fablabbcn/smartcitizen-kit-21
```

The _bootloader_ and _tools_ repositories are [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) of the main firmware so **you must do a `--recursive` clone** to get them.

!!! info
	I you download the code manually (with the _clone or download_ button on github) you will **not** get the [bootloader](https://github.com/fablabbcn/uf2-samdx1/tree/88aa54c1afab2647904aaccbe1a6b960c02fdb24) and [tools](https://github.com/fablabbcn/smartcitizen-tools) submodules code. To be able to compile the firmware you need to download the _tools_ submodule and place it in the proper folder.

## SAMD21 bootloader

If your kit doesn't have the bootloader already flashed (all the kits that we ship come with it) you will need an [ATMEL-ICE](https://www.digikey.es/en/product-highlight/a/atmel/atmel-ice-programmer-debugger) programmer. This process can also be done with a Raspberry Pi computer and the proper [connector](https://www.adafruit.com/product/2094) and cables, in [this guide](https://docs.smartcitizen.me/Guides/Debug%20the%20firmware/) you will find informtaion on how to do this.

![](/assets/images/sck_2/SCK21_data_connectors.png)

Connect the Atmel-ICE programmer to the 10 pin SWD connector and to your computer. Power the SCK via USB, you can use any USB charger or even your computer.

Open a terminal, go to the folder where you cloned the firmware repository and run:

```bash
cd smartcitizen-kit-21
./make.py boot
```

You will see a lot of output when compiling, the led on the SCK should _breath_ in **green** and you should see an output similar to this:

![](/assets/images/sck_2/flashing_bootloader.png)

You are ready for the next step, just remember to disconnect the Atmel-ICE programmer and connect the SCK to your computer with a USB cable.
 
## SAMD21 firmware
 
The bootloader we just flashed allows a very simple way of uploading the SCK firmware based on the [UF2](https://github.com/Microsoft/uf2) format, when you **double-click the reset button** of your kit it will expose a [MSD](https://en.wikipedia.org/wiki/USB_mass_storage_device_class) interface to your computer and a new drive will popup where you can just drag the compiled firmware file (converted to UF2 format).

![Reset button](/assets/images/sck_2/SCK21_Reset.png)

### Build script

![](/assets/images/sck_2/build_script_usage.png)

You can use the same script used to flash the bootloader (`make.py`) that will do everything for you: compile the firmware, convert the binary to UF2 format and upload it to the kit:

```bash
python3 make.py build flash sam
```

If this is your first time building the software, platformio will take a while installing all the needed dependencies, be patient. If there are no errors you should see an output similar to this:

![](/assets/images/sck_2/flashing_firmware.png)

A copy of the compiled software in UF2 format called _SAM_firmware.uf2_ will remain in the _bin_ folder. You can use this file to reflash your kit without compiling it again. 

!!!info
	If you have any problem you can enable verbose output by calling _build.py_ script with the `-v` flag. There is a **known issue** that causes first compilation to fail, if this happens please just try again.

### Manual install

If you want to install the firmware manually (or you had some problem with the build script) just follow this steps:

```bash
cd sam
pio run
```

After a lot of compilation messages you should see an output similar to this:

![](/assets/images/sck_2/pio_run.png)

then to convert the binary firmware to UF2 format do:

```bash
cd ..
./tools/uf2conv.py -o SAM_firmware.uf2 sam/.pio/build/sck2/firmware.bin
```

you should see something like this:

![](/assets/images/sck_2/uf2_conv.png)

Now **double-click the reset button of your kit** open your favorite file browser and drag the file you just created to the _SCK-2.0_ drive. The kit will reset and run the new firmware.

![](/assets/images/sck_2/drag_firmware.png)

!!! info
	Keep in mind that if your computer is not configured to automount new drives you will need to mount your sck manually ([as any other USB drive](https://linuxconfig.org/howto-mount-usb-drive-in-linux)).

## ESP8266 firmware

Just like the other parts of the process this is also covered by our `make.py` script. So you can just do:

```bash
python3 make.py build flash esp
```
As before, if this is the first time you do it, it will take a while on downloading dependecies and building the firmware.

In this case the upload process is different, since the ESP8266 chip is not connected to the USB interface the data must be uploadded through the SAMD21 chip.
Our [upload script](https://github.com/fablabbcn/smartcitizen-kit-21/blob/master/make.py) takes care of searching for a SCK on the USB bus, sending a command to the kit so it put's himself in what we call _bridge mode_ (white led) and uploading the firmware. This is the expected output:

![](/assets/images/sck_2/flashing_ESP_firmware.png)

!!! info
	Sometimes the ESP8266 and the uploader software don't get synced and the upload fails. Normally if you try again it will work. After first try you don't need to rebuild, you can just do `python3 make.py flash esp`.



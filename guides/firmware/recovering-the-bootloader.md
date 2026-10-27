<!-- Source: https://docs.smartcitizen.me/guides/firmware/recovering-the-bootloader/ -->

# Recovering SAMD21 bootloader

If your kit doesn't have the bootloaded flashed (all the kits that we ship come with it), or if it has lost it for a reason (bad USB cable for instance), you will need to recover the bootloader.

!!! info "What is the bootloader?"
    The bootloader is a small piece of code that lives inside the [Data Board SAMD21 microcontroller](https://docs.smartcitizen.me/hardware/boards/data-board.md#microcontrollers) that takes care of the initialisation of the core systems of the SAMD21. For instance, it starts communications via USB, and takes care of booting the first instructions of the [Smart Citizen firmware](https://docs.smartcitizen.me/hardware/firmware.md).

    Not having a bootloader, means that the device is practically _bricked_, the [status LED](https://docs.smartcitizen.me/hardware/kit/features.md#special-status) is GREEN, and we need to recover the bootloader.

!!! danger "Make sure you need to do this"
    This instructions only are needed if your kit doesn't have the bootloader already flashed.

## Equipment required

Typically you will need [ATMEL-ICE](https://www.digikey.es/en/product-highlight/a/atmel/atmel-ice-programmer-debugger) programmer.

!!! info
    This process can also be done with a Raspberry Pi computer and the proper [connector](https://www.adafruit.com/product/2094) and cables, in [this guide](https://docs.smartcitizen.me/guides/firmware/debug-the-firmware.md) you will find information on how to do this.

![](https://docs.smartcitizen.me/assets/images/sck-data-connectors.png)

## Steps

In order to flash the bootloader, follow the steps below:

1. Connect the Atmel-ICE programmer to the 10 pin SWD connector and to your computer.
2. Power the SCK via USB, you can use any USB charger or even your computer.
3. Open a terminal, go to the folder where you [cloned the firmware repository](https://docs.smartcitizen.me/guides/firmware/edit-the-firmware.md#getting-the-firmware) and run:

    ```
    > cd smartcitizen-kit-21
    > ./make.py boot
    ```

    !!! warning
        Make sure you have the necessary requirements for running the python script.

4. You will see a lot of output when compiling, the led on the SCK should _breath_ in **green** and you should see an output similar to this:

    ![](https://docs.smartcitizen.me/assets/images/sck_2/flashing_bootloader.png)


!!! success "Done with the bootloader"
    You are done with this step! The kit now needs to be reflashed. Follow the steps in the [firmware upgrade guide](https://docs.smartcitizen.me/guides/firmware/upgrading-the-firmware.md).
# Auxiliary connector

The [data board](/Components/Data Board/) features a standard [Grove connector](https://wiki.seeedstudio.com/Grove_System/) where external modules can be connected. The connector supports an independent I2C bus by default, but by software it can be configured to support other uses (GPIO, I2C and UART). It can supply power **up to 750mA**, and it can be enabled or disabled by software to save energy.

![](/assets/images/sck_2/SCK21_Aux.png)

!!!info "There is a lot more to it!"
    The Smart Citizen Kit is designed with a modular approach in mind. This means that the [Urban Board](/Components/Urban%20Sensor%20Board/) is only a selection of low cost sensors for air quality, but the hardware itself can be expanded for other use cases such as a more advanced air quality monitoring setup, soil monitoring, or water quality. Make sure you check our [guide on how to use them](/Guides/getting%20started/Third%20party%20sensors/).

## Supported sensors

{{ insert_cards(type="sensor", filter="type", value=["external"]) }}

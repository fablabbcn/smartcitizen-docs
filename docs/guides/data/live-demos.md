# Live demos

This guide is meant to show some possibilities for you to do _live demos_ with data. There are plenty of ways to do it, but in this guide we will focus on the following three:

TODO - GIF with graph

- Through the Serial (USB), either with [Arduino IDE](https://www.arduino.cc/en/software/) Serial Monitor (simple) or with [SerialStudio](https://serial-studio.github.io/) (more configurable plots)
- Via the online web dashboard available at [dashboard.smartcitizen.me](https://dashboard.smartcitizen.me), useful for _long-term_ displays

## Using Serial Tools

In this case, we will need a computer with either the [Arduino IDE](https://www.arduino.cc/en/software/) or [SerialStudio](https://serial-studio.github.io/). These tools will be used to plot the data coming from the kit (only one kit at a time), which will be connected via USB with a computer.

!!!info "Feeling creative?"
    If you rather use a more creative approach, you can follow [this guide](Creative coding) for using [processing](https://processing.org) to make these visualisations.

### Arduino IDE

After Arduino 2.0 version, you can see the _Serial Monitor_ and the _Serial Plotter_ at the same time. This is very useful to interact with the kit *and* see the data in real time, so we recommend upgrading to Arduino 2.0 for this. If not, you can always use Arduino 1.8.*, but you'll have to switch back and forth between the _Serial Monitor_ and the _Serial Plotter_.

![](/assets/images/arduino-ide-graph.png)

!!!info "Using the Shell"
    If you are not familiar with it yet, make sure you check the [Shell Guide](/guides/getting-started/using-the-shell) before the next steps.

!!!example "Step-by-step"
    * Connect to your SCK via the _Port_ selection
    * Open the _Serial Monitor_ and type in the _monitor_ command (avoiding the _milliseconds_ and _timestamp_ columns with the `-noms` and `-notime` options). In this example we will check the temperature by issuing the following command:
        ```
        monitor -noms -notime temperature
        ```
    * Open the _Serial Plotter_ and enjoy a nice looking graph!

### SerialStudio

[SerialStudio](https://serial-studio.github.io/) is a great tool for visualising data and make dashboards with your kit connected to a computer. It's more advanced than the Arduino Serial Monitor because you can customise how your data will be displayed, add graphs, widgets, and save the configuration for each device.

![](TODO)

!!!info "Examples"
    You can see the examples [here](/assets/serial_studio) TODO

## Using the web dashboard

For this, you can visit the [dashboard](https://dashboard.smartcitizen.me) with a particular ID. For instance, [this device](https://dashboard.smartcitizen.me/?id=15618).

You can toggle some options on the side menu, but by default you will have the _Auto Update_ check active. If the kit you are checking is sending data, updates should come little by little.

![](/assets/images/dashboard.png)

!!!info "No graphs? No problem!"
    If you don't want to see the graphs on the dashboard, you can remove them by deactivating the _Show Graphs_ on the side pannel. This will leave a neat view of the sensors. You can also choose which sensors, and their order, to clean up the view in case your kit has many sensors connected.

    ![](/assets/images/dashboard-no-graph.png)

In case you want to change the interval, so that data comes in more frequently, you can do so by [Using the Shell](/guides/getting-started/using-the-shell). To avoid checking that guide again, this is the command to issue if you want to read and publish the sensors every 5 seconds (which will send updates very quickly, although with a bit of delay because data needs to fly from your kit to the platform):

```
config -readint 5 -pubint 5
```

When you are done, make sure you reset the reading and publication interval back to normal, to avoid cluttering our beloved platform with unnecessary data **and to drain your kits battery**

```
config -readint 60 -pubint 180
```

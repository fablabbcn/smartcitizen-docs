# Air quality stations

## Hardware design

!!! warning "A note about versions"
    Some of the diagrams below are from older designs, but you they haven't changed much! Hopefully they are still understandable!

The Stations should come assembled and ready to use. They consist of various parts:

- [Enclosure and mounting system](#enclosure-and-mounting-system): for protection and support.
- Sensors module: contains the electronics and sensors, it can be accessed without having to uninstall the rain cover.
- [Power supply](#power): is separated from the main module, so that intervention in the sensors' area can be performed safely with a tangible desconection of the mains power.

![](/assets/images/station-small-exploded.png)

### Enclosure and mounting system

The enclosure holds the sensors in place and protects them against weather. A rain and sun radiation **cover** for additional protection can be used, which carries out the structural support of the station and protects the unit against rain, wind or heat.

![](/assets/images/station-v3-mounting.png)

!!! tip "Flexible attachment"
    This mounting is thought to work on a lampost, fence or wall. We recommend a somewhat flexible join (i.e. zip-ties) in case of windy locations.

The enclosure can be installed using the _mounting holes_ seen below. There is sufficient space to pass zip ties. If you want to use drills, we recommend at least 6mm screws (or 8mm) and to dissasemble the plastic cover from the sandwich pannel for safer installation.

## Deployment tips

Below are some general guidelines for the installation of the device:

- Avoid areas with moist accumulation when possible
- Avoid temperature and humidity transients
- Avoid covering the sensors in front of the sensors, specially the PM sensor
- Avoid covering the microphone and particles to go in the microphone port
- Avoid direct flow towards the sensors. If exposed under flow conditions, have the flow go parallel to the sensors' surface
- Despite the umbrella cover, sun radiation and transients are better to be avoided
- A good height for installing the sensors is somewhere between 2-3m, but it all depends on the case study and available support structures.

## Handling calibration data

Some components of the Station have individual calibrations such as the Alphasense Electrochemical Sensors. For this reason, it's necessary to store the physical ID (hardware ID) of the Station alonside to the virtual device in the Smart Citizen Platform. The harwdware ID should normally be in a sticker to the enclosure **both inside and outside** and looks like this:

```
SCAS2100XX
```

This number is important to relate to the actual calibration values of the sensors, stored in the [data repository](https://github.com/fablabbcn/smartcitizen-data/tree/master/hardware). In order to postprocess the data and calculate pollutants, make sure that the `Hardware ID` is safely stored in the platform's device, by posting this data to `postprocessing_info` field of the device. You can follow [these instructions](/guides/data/handling-calibration-data/) to store the `postprocessing_info` of your device.

All the data is sent in raw to the Smart Citizen Platform and it's then processed outside of the sensors themselves. Both raw, and processed data are kept on the platform and can be accessed at any time. Data can be published to other APIs or to [Zenodo](https://zenodo.org) as well, in case of research projects that seek contribution to Open Science Datasets.

!!! tip "More on the processing of the data"
    Check [this guide](/guides/data/custom-data-processing/) to learn more about how to postprocess the data of the sensors your own way.
# Smart Citizen API

The Smart Citizen API exposes the Platform functionalities over a clear REST API. It allows applications to be developed on easily on top having access to all the features to create complex and rich tools. The main instance is available at [api.smartcitizen.me](https://api.smartcitizen.me/). 

You can explore and contribute to the [source](https://github.com/fablabbcn/smartcitizen-api). This is free software available under GNU (Affero) General Public License (AGPL).

!!! info "TL;DR"
	Check the developers ready [**API Documentation**](https://developer.smartcitizen.me/)

## Data Ingestion Flow

The Platform supports multiple sensor types and even data coming from other platforms. On the following section, we describe all the features supported when it comes to sending data to the platform.

### Ingestion protocols

Two protocols are supported for data to be sent to the platform: MQTT and HTTP

- MQTT is the one used by constrained devices as the Citizen Sensors and the Living Lab Stations. It allows the devices to post data to the platform after they are registered. It also allows them to receive configuration options (i.e. sensors reading interval) and report errors (i.e. sensors are malfunctioning).
- HTTP is aimed at applications publishing data to the platform (i.e. an existing sensors platform that also wants to make all the data available to the platform). This API gives access to all the platform functionalities as it is part of the core Smart Citizen API. Over this API we are not just limited to publish data but to register new devices or even users.

oth protocols support transport encryption with TLS to ensure secure communication between the client and the server over the Internet.

### Authorisation and authentication

Knowing who posts what is a serious problem when it comes to hundreds of sensor data being published per minute. Constrained hardware devices using the MQTT API use a unique device token given to the device every time is registered on the platform. The token authenticates the devices against the platform, and it can be expired at any time to prevent a device to keep publishing. Instead, the HTTP API supports authentication using an OAuth2 or a private token. Both mechanisms work at a user level allowing a single process to manage all the devices created by a user.

### Kits blueprints

Each device sensors configuration needs to be previously registered on the platform to ensure each datapoint published is associated with the required metadata. This information is called a Kit blueprint. The minimal blueprint includes all the necessary data that a user might provide to create a Kit. It is composed of Components, and those can reuse existing Sensors and Measurements. Sensors are the hardware or software components that record the data. Measurements are descriptions of what the sensors are recording.

### Data Storage

Once the steps above are completed data is stored in a database cluster performing asynchronous masterless replication to ensure data backup and availability. Each datapoint is stored with the following items:

- _Component_: A reference to the component type that generated the datapoint.
- _Device_: A reference to the device that generated the datapoint.
- _Raw Data_: The datapoint as received to the platform
- _Processed Data_: The datapoint after applying post processing, when
implemented.
- _Timestamp_: The time the datapoint was generated.
Once stored historical data available via the Smart Citizen API. All the other services, as the Smart Citizen Webpage, access the data from there. The API also exposes a method where data is processed to a CSV file and email to the user. That allows loading the data offline to any software capable of dealing with CSV files (i.e. Microsoft Excel, MATLAB, etc.)

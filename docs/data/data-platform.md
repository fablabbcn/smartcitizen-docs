# Data Platform

The platform is a *front and backend* solution for ingesting, storing and interacting with data.

![](https://i.imgur.com/qiDKL0r.jpg)

The Data platform englobes services/tools with the following functionalities:

- [API](#api)
- [data ingestion](#data-ingestion) and [forwarding](#data-forwarding)
- [data storage](#data-storage)
- [data access](#data-access)
- [front-end applications](#front-end-applications)

!!! info "Have your own platform?"
	Check the possibilities to send data to other platforms in [this guide](/guides/data/Sending data to other platforms).

!!! warning "Are all systems operational?"
	Check the smartcitizen.me instance status in real time in the [uptimerobot.com](https://status.smartcitizen.me) dashboard.

## API

The Smart Citizen API exposes the Platform functionalities over a clear REST API. It allows applications to be developed on easily on top having access to all the features to create complex and rich tools. The main instance is available at [api.smartcitizen.me](https://api.smartcitizen.me/).

You can explore and contribute to the [source](https://github.com/fablabbcn/smartcitizen-api). This is free software available under GNU (Affero) General Public License (AGPL).

!!! info "TL;DR"
	Check the developers ready [**API Documentation**](https://developer.smartcitizen.me/)

## Data Ingestion

The Platform can ingest data from multiple sensor types and even data coming from other platforms. Two protocols are supported for data to be sent to the platform: MQTT and HTTP.

- MQTT is the one used by devices such as the Smart Citizen Kit and the  Stations. It allows the devices to post data to the platform with a secret `token` once the device is registered on the platform. Sensor data, and debugging information is sent over MQTT.
- HTTP is aimed at applications publishing data to the platform (i.e. uploading SD-card data, processing data asynchronously by external applications, or an external data platform that also wants to make all the data available on the Smart Citizen one). All of this can be done via the HTTP API. Over this API we are not just limited to publish data but to register new devices or even users.

!!! info ""
	Both protocols support transport encryption with TLS to ensure secure communication between the client and the server over the Internet.

## Data forwarding

For certain projects, data can also be forwarded to other platforms via MQTT. This is an *opt-in* experimental feature, and can be used to retrieve real-time data via MQTT, using th same JSON representation as the one in the API. This allows for connection to external platforms without needing to request via the API, since all the necessary information is available in the JSON representation.

!!! info "Existing integrations"
	Currently, we are working together with other colleagues on integrating modules so that data can be directly ingested into a [FIWARE](TODO) platform, or into a [OGC STAplus](TODO) platform. This allows incredible interoperability, leveraging the scalability of MQTT.

!!! info "Check the developer documentation"
	For more information and use cases, check the [developer](https://developer.smartcitizen.me) documentation.

## Authorisation and authentication

Devices using the MQTT API use a unique device `token` generated once the device is registered on the platform. The `token` authenticates the devices against the platform, and it can be expired at any time to prevent a device to keep publishing. Instead, the HTTP API supports authentication using an OAuth2 or a private token. Both mechanisms work at a user level allowing a single process to manage all the devices created by a user.

## Data storage

User and device metadata is stored on a SQL database (we use PostgresQL). Sensor readings (the timeseries) is stored in a database cluster performing asynchronous masterless replication to ensure data backup and availability. This is all available on the [API repository](https://github.com/fablabbcn/smartcitizen-api)

## Data access

All stored historical data is available via the Smart Citizen API. All the [front-end applications](#front-end-applications), such as the Smart Citizen Webpage, access the data from there.

The API also exposes a method where data is processed to a CSV file and email to the user. That allows loading the data offline to any software capable of dealing with CSV files (i.e. Microsoft Excel, MATLAB, etc.). The CSV format is different from that of the SD-card.

!!! info "Developer ready"
	Check the developer documentation to get more info on the API.

## Front-end applications

There are various applications that use the API to access data, or manage devices/user settings.

* **Smart Citizen Website**: the website provides an easy to interface where devices data can be accessed in near real time to facilitate the exploration, alongside other contextual information (maps, keywords, etc). It also provides an interface to manage devices, user information, and custom settings, such as email notifications, data policy settings, among other. The main instance its available at [smartcitizen.me/kits](https://smartcitizen.me/kits). You can explore and contribute to the [source](https://github.com/fablabbcn/smartcitizen-web). This is free software available under GNU Affero General Public License (AGPL).
* **Custom dashboards**: these custom dashboards are used to visualise data in a simpler, but more advanced ways, for instance, to display them in large screens. More on the [data tools](Data Tools) page!
* **Onboarding app**: the onboarding app facilitates the process of device setup to ensure that users, irrespective of technical expertise, can install start collecting data. It guides the user through the process of the setup using simple language and a friendly graphic interface. It is built as a separate tool from the core Smart Citizen Webpage in order it can be customized for each deployment. It exchanges data with the core platform using the Smart Citizen API. The main instance its available at [start.smartcitizen.me](https://start.smartcitizen.me). There are also customized instances for specific projects such us [onboarding.iscape.smartcitizen.me](https://onboarding.iscape.smartcitizen.me) or [start.decode.smartcitizen.me](https://start.decode.smartcitizen.me). You can explore and contribute to the [source](https://github.com/fablabbcn/smartcitizen-onboarding-app-start). This is free software available under a MIT License.

!!! tip "Check the guides"
	We prepared a series of guides to help you on the most common features you will use

	* [Onboarding Sensors](/guides/Onboarding Sensors)
	* [Uploading SD Card Data](/guides/Uploading SD Card Data)
	* [Downloading data](/guides/Downloading the Data)

!!! info "Want to build your own?"
	Check the developers ready [**API Documentation**](https://developer.smartcitizen.me/)

## Source files

Check the source below:

* Smart Citizen API: https://github.com/fablabbcn/smartcitizen-api
* Smart Citizen Web: https://github.com/fablabbcn/smartcitizen-web
* Onboarding App: https://github.com/fablabbcn/smartcitizen-onboarding
* Smart Citizen Data (python): https://github.com/fablabbcn/smartcitizen-data
* Smart Citizen Data (R): https://github.com/fablabbcn/smartcitizen-R-data
* Smart Citizen Flows: https://github.com/fablabbcn/smartcitizen-flows
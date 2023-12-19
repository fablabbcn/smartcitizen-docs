# Downloading the Data

Once you've added your SCK to the platform and it's capturing and sending data correctly, you can interact with the platform in several ways. Visualizing the data, downloading the data and interacting with the data through the API.

## Download Data

If you are interested in use the data captured by your sensors, you can download all the data for later use. To do this, go to your device page, at the bottom there is a button called *DOWNLOAD DATA*. You will receive an email with a link to download your data on <a href="https://en.wikipedia.org/wiki/Comma-separated_values" target="_blank">CSV</a> format in a minute or two.

![](/assets/images/kit-detail.png)

And then:

![](/assets/images/csv-download.png)

## API

The <a href="http://developer.smartcitizen.me/" target="_blank">Smart Citizen API</a> allows you to request back information from your devices and do incredible things with it.

It is a <a href="https://en.wikipedia.org/wiki/Representational_state_transfer" target="_blank">REST</a> API and it returns the information in <a href="https://en.wikipedia.org/wiki/Json" target="_blank">JSON</a> format. This means you can easily access the information from any language like Javascript, PHP, Processing.org, Python, and start doing things with it quickly.

### Using scripts

Python scripts are provided in the [scdata](https://pypi.org/project/scdata/) python package repository for downloading devices data in a programatic way. Make sure to [check the examples](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples) in the git repository.

!!! tip "Code examples"
	You can also find some examples on [smartcitizen-toolkit](https://github.com/fablabbcn/smartcitizen-toolkit) repository.
# SD-card storage

If you don't want to store data on the platform, or remote connectivity is not available for you, you can choose to store data on the SD-card.

By default, the [Data Board](/boards/Data Board) comes with a 16Gb micro SD-card, which can literally store years of data. Sensor data is stored in [CSV format](#sensor-readings). You will also find other files, which are described below, such as [hardware information](#hardware-information) or other special features, such as [debugging](#debugging), or the possibility to [access SD-card data via USB](#console-access).

## Sensor readings

Data is stored on the SD-card in CSV format, with a `comma` separator and `UTF-8` encoding. Each day, a different data file is stored on the onboard SD-card, named `YY-MM-DD.CSV` (for example, `24-05-01.CSV` would contain data from May 1st, 2024). In case the [Data Board](/hardware/boards/data-board) resets, it will generate an additional file for that day, and name it `YY-MM-DD-XX.CSV`, where `XX` are incremental numbers indicating the number of files (for example, `24-05-01-01.CSV` would contain data from May 1st, 2024, alongside with the previously generated file `2024-05-01.CSV`).

!!! warning "Many files with additional numbering?"
    This could be a symptom that the device is having hardware issues, as it may be rebooting more than usual!

!!! danger "Breaking change"
    As of firmware release `0.9.9`, the naming convention changed for these files. Previously, the naming was `YY-MM-DD.XX`, being `XX` the same as above. For convenience, the `.CSV` file extension was kept when `0.9.9` was released.

The file format for the sensor readings is as follows:

![](/assets/images/csv-format.png)

Below you can find what each row/rows mean, in order:

- `Short name`: Short name for the variable captured
- `Units`: units in which the measurement was taken
- `Description`: Short description for the variable captured
- `Sensor ID`: this row is necessary in case you want to upload data to the [Data Platform](/data/data-platform/). Do not delete or change this row, becase data may get all mixed up!
- `Data rows`: each row follows the same format, being the first column the `timestamp` in `ISO8601` and `UTC` format. Subsequent columns represent data, with `.` representing decimal numbers. Missing data is represented by `null`.

## Hardware information

Hardware information is stored in a file called `INFO.TXT`. This file can be used to retrieve firmware information, hardware versions, and some brief debugging information. The same information is available via the [API](https://api.smartcitizen.me/devices) (on `hardware>last_status_message`) and on the [mobile access point](/guides/firmware/upgrade-the-firmware/#make-a-back-up-of-your-info). This file contains the device serial number and the hardware and firmware versions and build dates for both microcontrollers:

```
Hardware Version: 2.1
SAM Hardware ID: <A-LONG-RANDOM-HASH>
SAM version: 0.9.7-5bbe51f
SAM build date: 2021-05-25T18:50:42Z
ESP MAC address: 8E:CE:4E:D5:62:45
ESP version: 0.9.2-5bbe51f
ESP build date: 2021-05-25T18:51:28Z
```

## Special features

### Console access

As of firmware `0.9.9`, you can access data via USB by using the [shell](/guides/getting-started/using-the-shell/). The `file` command can become very handy to access to SD-card data, without having to extract the SD-card.

```
SCK > help
...
file:        SD card file operations: [-ls] [-rm filename] [-less filename] [-allcsv]
```

You can list files by:

```
SCK > file -ls
Files found (date time size name):
2024-01-01 00:00        317 INFO.TXT
2024-01-01 00:00      17664 ERROR.TXT
2024-01-01 00:00       1585 24-11-19.CSV
2024-01-01 00:00      56448 24-11-20.CSV
...
```

Or output the content of a file (similar to `less` command on `linux`):

```
SCK > file -less 24-12-09_01.CSV

24-12-09_01.CSV
==============
TIME,TEMP,HUM,BATT,SDCARD,RSSI,LIGHT,NOISE_A,SEN5X_PM_1,SEN5X_PM_25,SEN5X_PM_4,SEN5X_PM_10,SEN5X_PN_05,SEN5X_PN_1,SEN5X_PN_25,SEN5X_PN_4,SEN5X_PN_10,SEN5X_TPSIZE,AS7331_UVA,AS7331_UVB,AS7331_UVA
ISO 8601,C,%,%,Present,dBm,lux,dBA,ug/m3,ug/m3,ug/m3,ug/m3,#/0.1l,#/0.1l,#/0.1l,#/0.1l,#/0.1l,um,uW/cm2,uW/cm2,uW/cm2
Time,Temperature,Humidity,Battery,SD card,WiFi RSSI,Light,Noise dBA,SEN5X PM 1.0,SEN5X PM 2.5,SEN5X PM 4.0,SEN5X PM 10.0,SEN5X PN 0.5,SEN5X PN 1.0,SEN5X PN 2.5,SEN5X PN 4.0,SEN5X PN 10.0,SEN5X Typical Particle Size,AS7331 UVA,AS7331 UVB,AS7331 UVC
,55,56,10,221,220,14,53,193,194,195,196,197,198,199,200,201,202,214,215,216
2024-12-09T12:20:05Z,21.49,42.12,-1,1,-63,176,40.77,2.90,3.00,3.00,3.00,1950.00,2270.00,2270.00,2270.00,2270.00,39.70,0.38,0.10,0.05
```

Remove a file (be careful):

```
SCK > file -rm 24-12-09_01.CSV
Deleting 24-12-09_01.CSV
```

Or output all files to `CSV` (this will take a while, be careful!!), note that there is no header between the files.

```
SCK > file -allcsv
```

!!! info "More on the shell guide"
    Check the [shell guide](/guides/getting-started/using-the-shell/) for more information.

### Debugging

If you are having issues with the hardware, and you want to read the [shell](/guides/getting-started/using-the-shell/) output, you can enable the `debug` interface by:

```
SCK > debug -sdcard
```

This will store all the `console` output from the kit into a `DEBUG.TXT`  file in the SD-card. Make sure you turn it of once done:

```
SCK > debug -sdcard
```

And check:

```
SCK > debug
...
```

!!! danger "This is an advanced feature"
    Make sure that you use this feature with caution and that you disable it after you are done.

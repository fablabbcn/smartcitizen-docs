# How to install and configure Orange to make data analysis

## Install Orange

!!! warning "Permisions"
    You might need admin permissions and you need internet connection

1. Go to the download page of Orange: https://orangedatamining.com/download/
2. Choose your OS and follow the instructions. In principle with the installation bundle you will be OK, no need to install it via CLI unless you know what you are doing or that you want to have full control

## Install add-ons

Once you have installed `Orange`,  open it and you will see something similar to this:

![](https://i.imgur.com/6BlZktR.png)

You can check the documentation, examples and tutorials from `Orange`. You can dismiss or use that documentation to get familiarized with `Orange`. 

We will need to install 3 add-ons:

* `Mecoda-orange`
* `Timeseries`
* `Geo` (in the case of using a GPS)

### Steps for installing

!!! info "Mecoda"
    [Mecoda](https://github.com/eosc-cos4cloud/mecoda-orange) is a package of widgets for Orange to access data from [Minka](https://minka-sdg.org/), [Odour Collect](https://odourcollect.eu/), [canAIRio](https://canair.io/), [Ictio](https://ictio.org/), [Natusfera](https://natusfera.gbif.es/) or [Smart Citizen](https://smartcitizen.me).

    These steps are also explained [here](https://github.com/eosc-cos4cloud/mecoda-orange/blob/master/docs/installation_and_user_guide.md)

1. Go to **Options** -> **Add-ons...** and you will see a window like this. We need to press "**Add more...**"

![](https://i.imgur.com/j3tDkUF.png)

2. You will see a pop-up window asking for the name.

![](https://i.imgur.com/ArwCdi7.png)

3. We write **"mecoda-orange"** and we press **add**.

4. Now we will find in the previous window a new addition called `Mecoda Orange`.

5. Now we need to select all the extensions that we want to install from the list.

6. When you sellect them in the collumn action it will hit **Install**.

![](https://i.imgur.com/smH9ABz.png)

7. After that we press OK. It may take some time to install the packages.

![](https://i.imgur.com/15f1HX9.png)

8. You may need to restart `Orange` for the changes to take effect. 

![](https://i.imgur.com/qbxH6I4.png)

## Check if everything is installed

If the installation was correct in `Orange`, in the panel to the left you will see new widgets available. (`MECODA`, `Time Series`, `Geo`)

![](https://i.imgur.com/jmwYmFv.png)

If you open MECODA, you will find the widgets for Smart Citizen (`Smart citizen Search` and `Smart Citizen Data`) among others. 

![](https://i.imgur.com/Q0AXXP4.png)

If everything is as expected, the add-ons are correctly installed.

# How to set up Processing and use serial to communicate with the Smart Citizen Kit

In this tutorial we'll go step by step through the setup of processing with a real time example of a Smart Citizen Kit

## Install processing

Go an download processing from the source: 
https://processing.org/download

And follow the steps for a regular installation. 



!!! info "Version used"
    This tutorial was done in 2023 with the version 4.2 for windows of Processing
    
    
You can find the code used in this tutorial here: https://github.com/fablabbcn/smartcitizen-docs/blob/master/docs/assets/pde/Flocks_example_serial/Flocks_example_serial.pde
    
    
## Find the right port

Depending on your configuration you will need to use this sketch:

```java 
// Example by Tom Igoe
import processing.serial.*;

// The serial port
Serial myPort;       

// List all the available serial ports
printArray(Serial.list());
```

Copy and paste this in a new sketch. Press the play button on the top left and you will see something like this:

![](https://i.imgur.com/ZzrBN5o.png)

In the console you will see one or more ports. You will have to select the one that has connected the Smart Citizen Kit.

For example:

```
[0] "COM3"
[1] "COM4"
[2] "COM6"
```

This is a notation of an array, where `0` means `COM3`, `1` means `COM4` and so on. We'll need to find which number (index) we need. In this case between 0, 1, and 2. 

### Using arduino IDE

If you have Arduino IDE installed, you can open it and check which port has the Smart Citizen Kit. To do that just open Arduino IDE and in the dropdown menu next to the verify and upload buttons. 

![](https://i.imgur.com/rqovYXy.png)

We're looking for the one that says "Arduino Zero(Native USB Port)" to know which name has. In this case `COM 6`

!!! info "Older version?"

    If you're using Arduino IDE 1.x and the interface is too different you can also access to this going to the menu Tools -> Port and you will find the same options. 

### Finding the array number

Once we have the name we need to look back in the array for finding the number that we need.

```
[0] "COM3"
[1] "COM4"
[2] "COM6"
```

In this case we need the number (the index) 2, because that points to **COM6**

## Example of use. The Flock of light

![](https://media.giphy.com/media/b5KYsvAUlcFDn1pyyj/giphy.gif)


Here we're going to see the code for doing this and how to make it work and a brief explanation of the serial communication part 

### The code

You can find the code used in this tutorial here: https://github.com/fablabbcn/smartcitizen-docs/blob/master/docs/assets/pde/Flocks_example_serial/Flocks_example_serial.pde

!!! info "Aknowledgements"

    The base code for this and more explanations about the Flocks can be found here: https://happycoding.io/tutorials/processing/creating-classes/flocking 

### Instructions to make it work

Find the number of the port that is explained above and look the part of the code (in the beggining, line 9) that has the constant PORT_INDEX and substitute with the number of the index of the port array. 


![](https://i.imgur.com/5MqGSL0.png)

In this example it's 2, but can be other integer number (probably from 0 to 2).


Now, if you press run it would work and the number of flocks will be equal to the amount of luxes that the SmartCitizen Kit recieves at any given moment (So you can pass your hand over it and you will see the flocks reduce their numbers). 

### Comments on the code. How does it work

#### Initializating serial

In the setup function (that runs only once) you can see something like this:

```java 
void setup() {
  String portName = Serial.list()[PORT_INDEX]; 
  smartCitizenKitSerial = new Serial(this, portName, 115200);
```

   Here we're setting the portName (`"COM4"`, `"COM3"`, etc) into an string from the list of available ports. We need it to instanciate the serial communication in the variable `smartCitizenKitSerial`. Here the constructor needs the parent (usually `this`), the name of the port and the baudrate. In the case of the Smart Citizen Kit: 115200. 
   
   
   !!! info "Other links of reference on Serial "


    Tutorial for connecting an Arduino and processing:  https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all
    
    
    Reference of Serial library on processing: 
    https://processing.org/reference/libraries/serial/index.html
    
   
   Then we're sending a parameter to the shell of the Smart Citizen Kit that it's going to answer us the data that we need in real time. 

```java 
  smartCitizenKitSerial.write("monitor light -notime -noms \n");
```

   This is the code for telling the SCK the following sentence:
   
   monitor: send the data in real time (main command)
       light (the light sensor specifically) 
       -notime (don't send the exact time with the sensor reading) 
       -noms (don't send the milliseconds between each reading)
    \n end of the line (Requirements by serial communication. )
    
 For more reference you can check [The guide about using the shell](https://docs.smartcitizen.me/Guides/getting%20started/Using%20the%20Shell/#set-recording-and-publication-intervals) or the [tutorial about monitoring in real time with arduino](https://docs.smartcitizen.me/Resources/Tutorials/Arduino%20Serial/#connect-to-your-kit) in which we use the same commands. 

 
 !!! success "Point  for customization :+1: "
 
     This is an easy spot for customization because changing this command we can switch from reading the light sensor to other sensors. 
     
#### Reading the serial

In the draw function from line 35 you can see this snippet:
```java 
 //Serial reading
  if ( smartCitizenKitSerial.available() > 0) 
  {  // If data is available,
  val = smartCitizenKitSerial.readStringUntil('\n');         // read it and store it in val
  println(val);

```
    
In this case we have to check if there is information available using `.available() > 0`. In that case we are going to read until we arrive to an end of the line, signified with `'\n'` using the method `readStringUntil` and we save it in the variable `val`

Then, for debugging porpuses we output the input that we recieve from the Serial port. 

After that you will see this part of the code, more related to the Flocks but also useful in how to treat the information. 

```java 
  Integer newNumberOfFlocks = numberOfFlocks;
  try {
    newNumberOfFlocks = Integer.parseInt(val.trim());
    if (newNumberOfFlocks < 0){
      newNumberOfFlocks = 1;
    }
  } catch (Exception e) {
  //do nothing   
  }
```

In this case we're going to get a string with a lot of spaces that we have to trim (using `trim` ) and parse it into a number that we have defined, that, in this case, control the number of Flocks. 

We use a try/catch boundary because in some other occassions we can recieve strings that are not just the numbers that otherwise they would raise an exception. 

The if newNumberOfFlocks < 0 we set it to 1 it's just depending on the logic of the flock system. 


#### Troubleshooting

If the program says that "port busy" is probably because you have another program using the serial monitor (such as arduino IDE)

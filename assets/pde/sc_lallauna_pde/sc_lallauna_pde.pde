// Noise Meter - A sketch for the STEAM Exhibition 
// IES La Llauna
// Co-Designed by Patricia Utrera and Xavier Domínguez
// Coded with love by @xavidominguez
//
// Instructions:
// - Connect SC Kit to the computer through Serial communication ( USB )
// - Add noise_level.jpg -> to the same folder of the sketch
// - Change the 0 to a 1 or 2 etc. to match your port using  printArray(Serial.list()); -> int PORT_INDEX = 2;
// - 

import processing.serial.*;


//Serial stuff
Serial smartCitizenKitSerial;  // Create object from Serial class
String val;     // Data received from the serial port
int PORT_INDEX = 2; //change the 0 to a 1 or 2 etc. to match your port using  printArray(Serial.list());


Integer noiseLevel=0;

PImage bg;

void setup() { 
  size (821, 996); 
  String portName = Serial.list()[PORT_INDEX]; 
  smartCitizenKitSerial = new Serial(this, portName, 115200);
  smartCitizenKitSerial.write("monitor Noise -notime -noms \n"); //here change light with noise or other sensors to get other data from the kit. 

  
  background(255);
  bg = loadImage("noise_level.jpg");
  
}

void draw() { 
  background(255);
  background(bg);
    //Serial reading
  if ( smartCitizenKitSerial.available() > 0) 
  {  // If data is available,
    val = smartCitizenKitSerial.readStringUntil('\n');         // read it and store it in val
    try{
      String n1 = val.trim();
      println(Integer.parseInt(n1.substring(0,2))); // Convert STRING value to an Integer -> see the Console to check the Noise value
      noiseLevel = Integer.parseInt(n1.substring(0,2));
    }catch (Exception e){
      // do nothing
    }
  }
  noStroke();
  
  if(noiseLevel<=40){
    fill(0,200,0);
  }else if((40<noiseLevel)&&(noiseLevel<60)){
    fill(255,165,0);
  }else{
    fill(200,0,0);
  }
  rectMode(CENTER);  // Set rectMode to CENTER
  rect(410, 910, 150, 25);
  rectMode(CORNER);  
  rect(400, 898, 25, -(noiseLevel*2.75));
  //rect(410, 856, 25, -noiseLevel*3);
  textSize(45);
  text(str(noiseLevel)+" dB", 95, 120); 

}

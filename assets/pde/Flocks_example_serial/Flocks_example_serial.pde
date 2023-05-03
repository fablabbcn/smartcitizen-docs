import processing.serial.*;

/*

Flock that grows and shrinks depending on how much light there is into a connected Smart Citizen Kit

INSTRUCTIONS

Check before  the name or the index of the serial port using printArray(Serial.list());


Aknowledgements: 


The basic structure of the flock is from this tutorial. 
https://happycoding.io/tutorials/processing/creating-classes/flocking


*/

Flocker[] flock = new Flocker[10000];
int numberOfFlocks = 3;

//Serial stuff
Serial smartCitizenKitSerial;  // Create object from Serial class
String val;     // Data received from the serial port
int PORT_INDEX = 2; //change the 0 to a 1 or 2 etc. to match your port using  printArray(Serial.list());


void setup() {
  //initialize serial
  String portName = Serial.list()[PORT_INDEX]; 
  smartCitizenKitSerial = new Serial(this, portName, 115200);
  smartCitizenKitSerial.write("monitor light -notime -noms \n"); //here change light with noise or other sensors to get other data from the kit. 

  size(600, 600);
  
  if (numberOfFlocks > flock.length)  numberOfFlocks = flock.length;
  for (int i = 0; i < numberOfFlocks; i++) {
    flock[i] = new Flocker();
  }

}

void draw() {

  background(200);
  if (numberOfFlocks > flock.length) numberOfFlocks = flock.length;
  for (int i = 0; i < numberOfFlocks; i++) {
    flock[i].step();
    flock[i].draw();
  }
  //Serial reading
  if ( smartCitizenKitSerial.available() > 0) 
  {  // If data is available,
  val = smartCitizenKitSerial.readStringUntil('\n');         // read it and store it in val
  println(val);
  Integer newNumberOfFlocks = numberOfFlocks;
  try {
    newNumberOfFlocks = Integer.parseInt(val.trim());
    if (newNumberOfFlocks < 0){
      newNumberOfFlocks = 1;
    }
  } catch (Exception e) {
  //do nothing   
  }
  if (newNumberOfFlocks != numberOfFlocks)
  {  
      //Add flocks
    for (int i = numberOfFlocks; i < newNumberOfFlocks; i++) {
      
      flock[i] = new Flocker();
    }
    //Update the number of flocks
    numberOfFlocks = newNumberOfFlocks;
    }
  } 

}



class Flocker {

  float x = random(width);
  float y = random(height);
  float heading = random(TWO_PI);
  float speed = random(1, 3); 
  float radius = random(10, 20);

  void step() {

    //find the closest Flocker
    float closestDistance = 100000;
    Flocker closestFlocker = null;
    for (int i = 0; i < numberOfFlocks; i++) {
      
      //make sure not to check against yourself
      if (flock[i] != this) {
        float distance = dist(x, y, flock[i].x, flock[i].y);
        if (distance < closestDistance) {
          closestDistance = distance;
          closestFlocker = flock[i];
        }
      }
    }

    float angleToClosest = atan2(closestFlocker.y-y, closestFlocker.x-x);

    //prevent case where heading is 350 and angleToClosest is 10
    if (heading-angleToClosest > PI) {
      angleToClosest += TWO_PI;
    } else if (angleToClosest-heading > PI) {
      angleToClosest -= TWO_PI;
    }

    //turn towards closest
    if (heading < angleToClosest) {
      heading+=PI/40;
    } else {
      heading-=PI/40;
    }

    //move in direction
    x += cos(heading)*speed;
    y += sin(heading)*speed;

    //wrap around edges
    if (x < 0) {
      x = width;
    }
    if (x > width) {
      x = 0;
    }

    if (y < 0) {
      y = height;
    }
    if (y > height) {
      y = 0;
    }
  }

  void draw() {
    ellipse(x, y, radius, radius);
  }
}

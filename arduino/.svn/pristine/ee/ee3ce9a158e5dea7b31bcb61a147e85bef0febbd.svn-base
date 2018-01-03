//Item Two-sensor Light
int sensorPin = 2; //IR sensor to be attached to digital pin NO.2
int ledPin = 13; //Digital LED-G to be attached to ditital pin NO.13

//variable sensorState for storing statistics about the status of the sensor
int sensorState = 0;

void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(sensorPin, INPUT);
}

void loop(){
  //Read statistics collected from the sensor
  sensorState = digitalRead(sensorPin);

  if(sensorState == HIGH){
    digitalWrite(ledPin, HIGH);
  }
  else{
    digitalWrite(ledPin, LOW);
  }
}


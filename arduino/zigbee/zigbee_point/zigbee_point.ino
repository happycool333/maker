//用于传感器终端的zduino
int sensorPin = 2; //IR sensor to be attached to digital pin NO.2
int ledPin = 13; //Digital LED-G to be attached to ditital pin NO.13

//variable sensorState for storing statistics about the status of the sensor
int sensorState = 0;

unsigned char havePerson[8] = {0xfe, 0x05, 0x91, 0x90, 0x53, 0x0d, 0x01, 0xff};
int inMonitor = 0; //0 already left, 1 in monitor

void setup() {
  
  Serial.begin(115200); //RX TX serial port
  
  pinMode(ledPin, OUTPUT);
  pinMode(sensorPin, INPUT);
}

void loop() {
  sensorState = digitalRead(sensorPin);
  if(sensorState == HIGH)
  {    
    //send data from serial port
    if(inMonitor == 0)
    {
      Serial.write(havePerson, 8);
      inMonitor = 1; //high level for time when someone in monitor.
    }
    digitalWrite(ledPin, HIGH);
  }else
  {
    inMonitor = 0; //someone left
    digitalWrite(ledPin, LOW);
  }

  delay(500);
}


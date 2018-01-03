// hardware:Zduino pro mini
//Zduino pro mini only has one serial.

// this program is used to control car
// zigbee as communication protocol throgh DL-LN33

unsigned char returnFlag[8] = {0xfe, 0x05, 0x91, 0x90, 0x14, 0x10, 0x01, 0xff};
int input1 = 5; // 定义uno的pin 5 向 input1 输出   
int input2 = 6; // 定义uno的pin 6 向 input2 输出  
int input3 = 9; // 定义uno的pin 9 向 input3 输出  
int input4 = 10; // 定义uno的pin 10 向 input4 输出  
int carState = 1;

void setup() {
  Serial.begin(115200); //RX TX serial port
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(8, OUTPUT);

  //初始化各IO,模式为OUTPUT 输出模式  
    pinMode(input1,OUTPUT);  
    pinMode(input2,OUTPUT);  
    pinMode(input3,OUTPUT);  
    pinMode(input4,OUTPUT);  

}

String myPtHex(int g){ // 把 g 最右邊 byte 印成 Hex 倆位
  String ret = "";
   int a = g& 0xf0;  // 左邊 4 bits
   a = a >> 4;  // 右移 4 bits
   int b = g& 0x0f;  // 右邊 4 bits
   char c = a < 10 ? a + '0' : a + 'A' - 10;
//   Serial.print(c);
   ret += c;
   c = b < 10 ? b + '0' : b + 'A' - 10;
//   Serial.print(c);
   ret += c;
//   Serial.print("#" + ret + "#");
   return ret;
}

void blinkLed(int pinNumber){
  digitalWrite(pinNumber, HIGH);
  delay(1);
  digitalWrite(pinNumber, LOW);
}

void loop() {

  // have zigbee data to come
  int dataIndex = 1;
   if (Serial.available()) {
    digitalWrite(LED_BUILTIN, HIGH); 

    //send back to zigbee board.
//    Serial.write(returnFlag, 8);
    
    myPtHex((char)Serial.read());  
    dataIndex ++;
    while(Serial.available()){
      String dataFlag = myPtHex((char)Serial.read()); 
      if(dataIndex == 7){
//        Serial.print("$"+dataFlag);

//if zigbee send data 01, start car.
        if(dataFlag == "01"){
          blinkLed(8);
          carState = 1;
        }
        // if zigbee send data 00, start car.
        if(dataFlag == "00"){
          blinkLed(8);
          carState = 0;
        }
      }
      dataIndex ++;
      
    }

    digitalWrite(LED_BUILTIN, LOW);
    
   }

    
  if(carState == 0){
    stopCar();
  }
  
  if(carState == 1){
    startCar();
  }

}



void startCar(){
  //forward 向前转  
      digitalWrite(input1,HIGH); //给高电平  
      digitalWrite(input2,LOW);  //给低电平  
      digitalWrite(input3,HIGH); //给高电平  
      digitalWrite(input4,LOW);  //给低电平
      delay(1000);  //延时0.5秒    
}

void stopCar(){
     digitalWrite(input1,LOW);  
     digitalWrite(input2,LOW);    
     digitalWrite(input3,LOW);  
     digitalWrite(input4,LOW);
     delay(1000);  //延时0.5秒      
}




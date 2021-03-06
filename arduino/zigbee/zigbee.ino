
unsigned char sendCmd[8]={0xfe, 0x05, 0x91, 0x90, 0x14, 0x10, 0x02, 0xff};//LN33 向


void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600); //USB serial port
  Serial1.begin(115200); //RX TX serial port

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

   if (Serial1.available()) {
    digitalWrite(LED_BUILTIN, HIGH); 

    Serial1.write(sendCmd, 8);
    
//    Serial.println(Serial1.read(),HEX); 
    myPtHex((char)Serial1.read());  
    while(Serial1.available()){
      myPtHex((char)Serial1.read()); 
    }
   }

   delay(100);   
   digitalWrite(LED_BUILTIN, LOW);
   delay(100);
}

void myPtHex(int g){ // 把 g 最右邊 byte 印成 Hex 倆位
   int a = g& 0xf0;  // 左邊 4 bits
   a = a >> 4;  // 右移 4 bits
   int b = g& 0x0f;  // 右邊 4 bits
   char c = a < 10 ? a + '0' : a + 'A' - 10;
   Serial.print(c);
   c = b < 10 ? b + '0' : b + 'A' - 10;
   Serial.print(c);
}


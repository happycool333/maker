# -*- coding: utf-8 -*  
import RPi.GPIO
import time
import serial
startCmd = [0xfe, 0x05, 0x91, 0x90, 0x53, 0x0d, 0x01, 0xff]
stopCmd = [0xfe, 0x05, 0x91, 0x90, 0x53, 0x0d, 0x00, 0xff]
ser = serial.Serial('/dev/ttyUSB0',115200)
ser.write(stopCmd)

def control_car():
  # 按钮输出针脚连接的GPIO口
  btnR = 21
  RPi.GPIO.setmode(RPi.GPIO.BCM)

  # 按钮连接的GPIO针脚的模式设置为信号输入模式，同时默认拉高GPIO口电平，
  # 当GND没有被接通时，GPIO口处于高电平状态，取的的值为1
  # 注意到这是一个可选项，如果不在程序里面设置，通常的做法是通过一个上拉电阻连接到VCC上使之默认保持高电平
  RPi.GPIO.setup(btnR, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)

  car_state = 0
  button_status = 0 #0：弹起 1：按下
  is_button_press = False

  while True:
    time.sleep(0.01)
    if (RPi.GPIO.input(btnR) == 0):
      if(button_status == 1):
        is_button_press = True
      button_status = 0
    else:
      button_status = 1
        

    if(is_button_press):
      if(car_state == 0):
        #发送启动消息
        print('start car')
        ser.write(startCmd)
        car_state = 1
      else:
        #发送停止消息
        print('stop car')
        ser.write(stopCmd)
        car_state = 0

      is_button_press = False

if __name__ == '__main__':
  control_car()
 

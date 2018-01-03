# -*- coding: utf-8 -*  
import serial
import time
import binascii

# 打开串口  
#ser = serial.Serial("/dev/ttyAMA0", 115200)
ser = serial.Serial("/dev/ttyUSB1", 115200)

outTime = 0
inTime = 0

def main():  
    while True:  
        # 获得接收缓冲区字符  
        count = ser.inWaiting()  
        if count != 0:  
            # 读取内容并回显  
            recv = ser.read(count)            
            ser.write(recv)
            parseZigbee(recv)
        # 清空接收缓冲区  
        ser.flushInput()  
        # 必要的软件延时  
        time.sleep(0.1)

def parseZigbee(recvBytes):

    global inTime
    global outTime

    currTimeInt = time.time()
    currTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(currTimeInt))
    print "%s: msg:%s" % (currTime, binascii.b2a_hex(recvBytes))

    #get zigbee address
    addr = recvBytes[4:6]
    addrStr = binascii.b2a_hex(addr)

    if addrStr == '1410':        
        outTime = currTimeInt
    if addrStr == '860d':        
        inTime = currTimeInt

    print 'inTime:%d' % inTime
    print 'outTime:%d' % outTime

    timeDist = (inTime - outTime)
    if timeDist > 0 and timeDist < 3:
        print '%s $$$$$$$ have one persion come in.' % currTime

    if timeDist < 0 and timeDist > -3:
        print '%s $$$$$$$ have one persion come out.' % currTime

def test(addr):
    global inTime
    global outTime
    print "test"

    currTimeInt = time.time()
    #print currTimeInt

    if addr == '1410':
        outTime = currTimeInt
    if addr == '860d':
        inTime = currTimeInt

    print inTime
    print outTime

    timeDist = (inTime - outTime)
    if timeDist > 0 and timeDist < 3:
        print 'have one persion come in.'

    if timeDist < 0 and timeDist > -3:
        print 'have one persion come out.'
    
     
if __name__ == '__main__':  
    try:  
        main()
        #test("1410")
        #time.sleep(2)
        #test("860d")
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  

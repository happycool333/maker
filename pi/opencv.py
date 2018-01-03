#coding:u8
# created by Huang Lu
# 27/08/2016 17:05:45 
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np
import time
from tempfile import TemporaryFile

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

import logging as log
from logging.handlers import RotatingFileHandler

#define log
rthandler = RotatingFileHandler('client.log', maxBytes=10*1024*1024, backupCount=5)
formatter = log.Formatter('%(threadName)s %(thread)d %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
rthandler.setFormatter(formatter)
logInst = log.getLogger('')
logInst.addHandler(rthandler)
logInst.setLevel(log.INFO)

ch = log.StreamHandler()
ch.setLevel(log.INFO)
ch.setFormatter(formatter)
logInst.addHandler(ch)

def uploadFile(imFile):
    # 在 urllib2 上注册 http 流处理句柄
    register_openers()
 
    # 开始对文件 "DSC0001.jpg" 的 multiart/form-data 编码
    # "image1" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置
 
    # headers 包含必须的 Content-Type 和 Content-Length
    # datagen 是一个生成器对象，返回编码过后的参数
    #imFile = open("test.png", "rb")
    datagen, headers = multipart_encode({"uploadedFile": imFile})
 
    # 创建请求对象
    request = urllib2.Request("http://172.27.35.1:8080/upload", datagen, headers)
    # 实际执行请求并取得返回
    print urllib2.urlopen(request).read()


cap = cv2.VideoCapture(0)
counter = 1
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    fileName = str(counter) + '.png'
    cv2.imwrite(fileName, frame)

    #outfile = TemporaryFile()
    #np.save(outfile, frame)

    #uploadFile(outfile)
    log.info('start to upload file.')
    uploadFile(open(fileName, "rb"))
    log.info('end to upload file.')

    if counter == 5:
        counter = 1
    counter += 1
    
    time.sleep(1)
cap.release()
cv2.destroyAllWindows() 

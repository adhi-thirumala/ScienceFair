from darkflow.net.build import TFNet
import cv2

from io import BytesIO
import time
import requests
from PIL import Image
import numpy as np

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


options = {"model": "yolov2-tiny.cfg", "load": "yolov2-tiny.weights", "threshold": 0.8}


tfnet = TFNet(options)

birdsSeen = 0
def handleBird():
    pass

while True:
    img = open("/home/adhit/Downloads/hhh.png")
    img = cv2.imread("/home/adhit/Downloads/hhh.png")

    # uncomment below to try your own image

    result = tfnet.return_predict(img)
    
    for detection in result:
        if detection['label'] == 'bird':
            print("bird detected")
            birdsSeen += 1
            curr_img.save('%i.jpg' % birdsSeen)

            time.sleep(8)

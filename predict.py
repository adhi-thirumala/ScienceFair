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
    r = requests.get('ip address of pi') # replace with your ip address
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    result = tfnet.return_predict(curr_img_cv2)
    print(result)
    for detection in result:
        if detection['label'] == 'bird':
            print("bird detected")
            #birdsSeen += 1
            curr_img.save('%i.jpg' % birdsSeen)
            fromaddr = "address u want to send from"
            toaddr = "address u want to send to"

            msg = MIMEMultipart()

            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "SUBJECT"

            body = "BODYTEXT"

            msg.attach(MIMEText(body, 'plain'))

            filename = '%i.jpg' % birdsSeen
            attachment = open('%i.jpg' % birdsSeen, "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "email password")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            #print (detection['label'])
            print('running again')
            time.sleep(4)

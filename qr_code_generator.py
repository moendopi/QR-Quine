import qrcode
import cv2
import os

#For shiggles
# The largest amount of characters that can be stored in a QR code is a 177 x 17 matrix holding 
# 4296 characters or 7089 numeric characters 

text = ''
with open("H:/QRCode/qr_code_generator.py", 'r') as this_program: # replace the path with wherever you want this to be
    text = this_program.read()

img = qrcode.make(text)
img.save("this_program.jpg")

decoder = cv2.QRCodeDetector()
val, points, straight_qrcode = decoder.detectAndDecode(cv2.imread("this_program.jpg"))

with open("H:/QRCode/self_execute.py", 'w') as self_execute: # replace the path with wherever you want this to be
    for line in text:
        self_execute.write(line)

#os.system('python self_execute.py) # in case you want an infinte loop
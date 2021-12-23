import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = '../pictures/2.jpg'

reader = easyocr.Reader(['en'])
ocr_result = reader.readtext(IMAGE_PATH,paragraph="False")

# filtering the results

products_result = []
for i in ocr_result:
    if i[1].isupper():
        products_result.append(i[1])

print(products_result)


# visualizing the results

"""

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
spacer1 = 100
spacer2 = 100
for detection in ocr_result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(spacer1,spacer2), font, 1,(0,255,0),2,cv2.LINE_AA)
    spacer1+=30
    spacer2+=30

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

"""
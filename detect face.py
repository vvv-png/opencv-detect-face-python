import cv2
import sys
img = cv2.imread(cv2.samples.findFile('the path to the image file'))#example (/users/username/desktop/image.jpg)
if img is None:
    sys.exit("Could not read the image.")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
head=cv2.CascadeClassifier('head.xml')#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
found = hand.detectMultiScale(img_gray,1.1,4)
amount_found = len(found)

if amount_found != 0:
	

	for (x, y, width, height) in found:
		# We draw a green rectangle around
		# every recognized sign
		cv2.rectangle(img, (x, y),
		              (x + height, y + width),
		              (0, 255, 0), 5)
		cv2.putText(img,"face",(x,y-5),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,0))#you can change the color with new rgb code
cv2.imshow("display window",img)
k=cv2.waitKey(0)

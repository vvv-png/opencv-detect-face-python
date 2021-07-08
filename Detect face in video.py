import cv2
vid = cv2.VideoCapture(0)
while True:
	ret, img = vid.read()
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	hand = cv2.CascadeClassifier('haad.xml')#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
	found = hand.detectMultiScale(img_gray, 1.1, 4)
	amount_found = len(found)
	for (x, y, width, height) in found:
		cv2.rectangle(img, (x, y),
		(x + height, y + width),
		(0, 255, 0), 5)
		cv2.putText(img,"face",(x,y-5),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,0))
	cv2.imshow("amir",img)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
		cv2.destroyAllWindows()

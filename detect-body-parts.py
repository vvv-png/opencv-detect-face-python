import cv2
vid = cv2.VideoCapture(0)
hand = cv2.CascadeClassifier('hand.xml')#https://raw.githubusercontent.com/Balaje/OpenCV/master/haarcascades/hand.xml
while True:
	ret, img = vid.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	haad = cv2.CascadeClassifier('haad.xml')#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
	eye = cv2.CascadeClassifier('eye.xml')#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
	found = haad.detectMultiScale(gray, 1.1, 4)
	found_hand = hand.detectMultiScale(gray, 1.1, 4)
	for (x,y,w,h) in found_hand:
		cv2.rectangle(img, (x, y),
		              (x + h, y + w),
		              (0, 255, 0), 5)
		cv2.putText(img, "hand", (x, y - 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 0))
	for (x, y, w, h) in found:
		cv2.rectangle(img, (x, y),
		(x + h, y + w),
		(0, 255, 0), 5)
		cv2.putText(img,"face",(x,y-5),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,0))
		roi_gray = gray[y:y + h, x:x + w]
		roi_color = img[y:y + h, x:x + w]
		eyes = eye.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
			cv2.putText(roi_color, "eye", (ex, ey - 5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=(255,0,0))
	cv2.imshow("amir",img)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
		cv2.destroyAllWindows()

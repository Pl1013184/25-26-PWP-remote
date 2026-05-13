import cv2, numpy
import time
import cvclass
#from apiserver import alien_is_there
factor=1.001
#face_classifier = cv2.CascadeClassifier(
#    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
#)


def getimgs():
	image=cv2.imread('wanted.jpg',0)
	faces=[]
	print('loading img, wait a few seconds')
	for i in range(900):
		#for x,y,w,h in face_classifier.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30)):
		face=image[:,:]
		cv2.resize(face,(900,900))
		cv2.dilate(face,(3,3),iterations=1)
		cv2.erode(face,(3,3),iterations=1)
#		cv2.equalizeHist(face)
			#cv2.GaussianBlur(face,(3,3),0)
			#if i==34:
			#	cv2.imshow('ts',face)
			#	cv2.waitKey(10000)
		faces.append(face)
		if i==899:
			print("image loaded-noerror")
	np_img=numpy.array(faces,'uint8')
	np_id=numpy.asarray(range(900))
	return np_img,np_id
def setup():
	x,y=getimgs()
	global recognizer
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.train(x,y)
	#save 
	print('recognizer trained')
	#recognizer.save("find_alienman.yml")
def finder(path_to_foto,pathing_):
	test=cvclass.cvcol(path_to_foto,gray=True,pathing=False)
	init_ts=cvclass.cvcol(path_to_foto,pathing=False)
	#init_ts.bigger(3)
	#recognizer= cv2.face.LBPHFaceRecognizer_create()
	#recognizer.read("find_alienman.yml")
	test.bluredlines()
#	print('proccessing image for clarity')
	for x in range(5):
		test.dialate()
		test.erode()
		#test.bigger(1.1)
	#test.bigger(3)
	#label_id, confidence = recognizer.predict(test.ret())
	#print(confidence)
	#faces=face_classifier.detectMultiScale(test.ret(),scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
	end_frame= cv2.cvtColor(test.ret(), cv2.COLOR_BGR2GRAY)
	#cv2.imshow('test',init_ts)
	#cv2.waitKey(10000)
	print('here')
	intz_tm=time.time()
	#print('found all faces')
	aOIest=end_frame
	id,cofind=recognizer.predict(aOIest)
	print('there',time.time()-intz_tm)
	print(f"Confidence Score: {cofind}")
	if cofind>166:
		print('we are not alone')
#		alien_is_there(True)
#		cv2.rectangle(init_ts.ret(), (x,y),(x+w,y+h),(0,255,0),2)
			#cv2.imshow('finally',init_ts.ret())
			#x=cv2.waitKey(20000)
		return init_ts.ret(),True
	else:
		return init_ts.ret(),False
setup()
def detect_face(frame):
	return finder(frame,False)

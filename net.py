import numpy as np
import cv2
from keras.preprocessing import image
import time

#-----------------------------
#opencv initialization
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#-----------------------------
#face expression recognizer initialization
from keras.models import model_from_json
model = model_from_json(open("model.json", "r").read())
model.load_weights('weights.h5') #load weights
#-----------------------------

emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

def analysis(data):
	img = np.reshape(data['data'], (data['height'], data['width'], 4)).astype('uint8')
	img = cv2.resize(img, (640, 360))
	img = img[0:308,:]

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	results = []

	for (x,y,w,h) in faces:
		if w > 130: #trick: ignore small faces
			detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
			detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
			detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48
			
			img_pixels = image.img_to_array(detected_face)
			img_pixels = np.expand_dims(img_pixels, axis = 0)
			
			img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

			predictions = model.predict(img_pixels) #store probabilities of 7 expressions
			results.append(predictions)
	return results

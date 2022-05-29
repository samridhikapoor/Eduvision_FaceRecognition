from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
from covid import Covid
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='7d125ba012bc447681da91239d255267')

covid = Covid()

prototxtPath = "face_detector/deploy.prototxt"
weightsPath = "face_detector/res10_300x300_ssd_iter_140000.caffemodel"

faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

maskNet = load_model("mask_detector.model")

def get_news():
    articles = newsapi.get_top_headlines(q='covid')['articles']

    final = []

    for i in articles:
        final.append([i['title'], i['description'], i['url'], i['urlToImage']])

    return final

def get_countries():
    k = covid.get_data()
    k = sorted(k, key = lambda i: i['confirmed'], reverse= True)
    countries = []
    cases = []
    deaths = []

    for i in k:
        countries.append(i['country'])
        cases.append(i['confirmed'])
        deaths.append(i['deaths'])
    return [countries, cases, deaths]

def get_total():
    active = covid.get_total_active_cases()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()
    return [active, confirmed, recovered, deaths]


def predict(frame, faceNet, maskNet):
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
		(104.0, 177.0, 123.0))
	faceNet.setInput(blob)
	detections = faceNet.forward()
	faces = []
	locs = []
	preds = []
	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		if confidence > 0.4:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	return (locs, preds)

def process(frame):
	frame = imutils.resize(frame, width=1080)
	(locs, preds) = predict(frame, faceNet, maskNet)
	num_mask = 0
	num_no_mask = 0
	for (box, pred) in zip(locs, preds):
		
		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred

		if mask > withoutMask:
			label = "MASK"
			num_mask += 1
		else:
			label = "NO MASK"
			num_no_mask += 1
		
		if label == "MASK":
			color = (0, 255, 0)
		else:
			color = (0, 0, 255)

		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	return frame, num_mask, num_no_mask

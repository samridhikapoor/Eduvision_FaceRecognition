from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn
import cv2
from predict import process, get_total, get_countries, get_news
from flask import Flask, render_template, Response

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("index1.html")
    else:
        # pass # unknown
        return render_template("index1.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index1.html")
    else:
        # pass # unknown
        return render_template("index1.html")

@app.route("/attendance", methods=['GET', 'POST'])
def att():
    return render_template("attendance.html")

@app.route("/numplate", methods=['GET', 'POST'])
def numplate():
    return render_template("numplate.html")

@app.route("/numplateprog", methods=['GET', 'POST'])
def numplateprog():
    return render_template("numplate_prog.html")

@app.route("/mask", methods=['GET', 'POST'])
def mask():
    return render_template("mask.html")

@app.route("/alert", methods=['GET', 'POST'])
def alert():
    return render_template("alert.html")

@app.route("/noplate", methods=['GET', 'POST'])
def index1():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Number Plate') == 'Number Plate':
            # pass
            # d_dtcn()
            return render_template("test.html")
    else:
        # pass # unknown
        return render_template("index.html")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        
        success, image = self.video.read()
        image, num_mask, num_no_mask = process(image)
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera')
def camera():
    return render_template('elements.html')

@app.route('/feed')
def feed():
    news = get_news()
    return render_template('feed.html', 
                            news=news)

if __name__ == "__main__":
    app.run(port=7000)
    
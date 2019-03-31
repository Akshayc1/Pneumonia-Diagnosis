from flask import Flask, render_template, url_for, request, session, jsonify
from werkzeug.utils import secure_filename
import os
from keras.models import load_model
import cv2
import numpy as np
from keras import backend as K


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.secret_key = os.urandom(24)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
	if request.method == 'POST':  # if the file is submitted post request is send using ajax
		file = request.files['file']
	target = os.path.join(APP_ROOT, 'static/images/')
	# print("Hello World")
	# print(file)
	filename = secure_filename(file.filename) 
	session['img'] = filename
	destination = "/".join([target, filename]) 
	file.save(destination)  
	target = os.path.join(APP_ROOT, 'images/')
	print(target)
	img_src = session['img']
	model = load_model('model.h5')
	image = cv2.imread("static/images/{}".format(img_src))
	input_image = cv2.resize(image, (256, 256))
	input_image = input_image / 255.
	input_image = input_image[:,:,::-1]
	input_image = np.expand_dims(input_image, 0)
	result = model.predict(input_image)
	K.clear_session()
	normal = str(result[0][0])
	pneumonia = str(result[0][1])
	dic = {'x': normal, 'y':pneumonia}
	return jsonify (dic)

if __name__ == '__main__':
	app.run(debug = True)
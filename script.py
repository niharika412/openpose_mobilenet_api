from flask import Flask , render_template ,request , url_for, redirect
import os
from pose import *
from PIL import Image
import cv2


app = Flask(__name__)
UPLOAD_FOLDER = './static/image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
	return render_template("index.html")


@app.route("/success", methods=['POST'])

def upload_file():
			content = request.files['file']
			content.save(os.path.join(app.config['UPLOAD_FOLDER'], content.filename))

						#load in content
			#print(os.path.join(app.config['UPLOAD_FOLDER'], '/content.jpg'))
			#content = ('./static/image/upload/'+content.filename)
			x=imgkeypoints('./static/image/'+content.filename)
			#x.save("target.jpg")
			#files=[content.filename,'target.jpg']
			return render_template('success.html',filename1=content.filename,filename2=content.filename.replace(".jpg","o.jpg").replace(".jpeg","o.jpeg"))

							
@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='image/' + filename), code=301)

if __name__ =="__main__":
	app.run(debug=True)

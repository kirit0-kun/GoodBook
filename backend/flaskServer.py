import os
from flask import Flask, render_template, request
from OCR.text_recognition import recognize_text
from scrape import scrape


app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/mahmoud")
def salvador():
    return "Hello, Mahmoud"

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg')#file.filename)
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    print('file uploaded successfully')
    text = recognize_text()
    print(text)
    print(scrape(text))
    return scrape(recognize_text())[0]
    #return 'file uploaded successfully'

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)



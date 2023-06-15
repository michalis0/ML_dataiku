export FLASK_APP=main.py

google cloud
CLOUDSDK_PYTHON=/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
gcloud app deploy
gcloud app browse


**Deploy without a problem using this in the main.py**

from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html', videos='YES IT DOES')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


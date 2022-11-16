import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from markupsafe import escape
import joblib
import inputScript

app = Flask(__name__)

model = joblib.load('Phishing_Website.pkl')

CORS(app)

@app.route('/', methods=['GET'])
def predict():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictphishing():
    url = request.form['url'] 
    checkprediction = inputScript.main(url) 
    prediction = model.predict(checkprediction) 
    
    if(prediction==1): 
        pred="Your are safe!! This is a Legitimate Website."
    else:
        pred="You are on the wrong site. Be cautious!" 
    
  
    return render_template("predict.html", prediction_text = '{}'.format(pred), url = url)

@app.route('/predict_api', methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.predictphishing([np.array(list(data.values()))])

    output=prediction[0]
    output.reshape(-1, 1)
    return jsonify(output)  

if __name__ == '__main__':
    app.run()


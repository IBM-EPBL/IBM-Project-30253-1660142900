import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import inputScript

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "OE-QJR_dqYubToiS8a2z_bokArc9V_t10jO1Pf0pja46"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictphishing():
    url = request.form['URL'] 
    checkprediction = inputScript.main(url) 

    data=checkprediction
    v=data([np.array(list(data.values()))])

     
    
    
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {
        "input_data": [
                {
                        "field": [
                                "index",
                                "having_IPhaving_IP_Address",
                                "URLURL_Length",
                                "Shortining_Service",
                                "having_At_Symbol",
                                                                "double_slash_redirecting",
                                "Prefix_Suffix",
                                "having_Sub_Domain",
                                "SSLfinal_State",
                                "Domain_registeration_length",
                                "Favicon",
                                "port",
                                "HTTPS_token",
                                "Request_URL",
                                "URL_of_Anchor",
                                "Links_in_tags",
                                "SFH",
                                "Submitting_to_email",
                                "Abnormal_URL",
                                "Redirect",
                                "on_mouseover",
                                "RightClick",
                                "popUpWidnow",
                                "Iframe",
                                "age_of_domain",
                                "DNSRecord",
                                "web_traffic",
                                "Page_Rank",
                                "Google_Index",
                                "Links_pointing_to_page",
                                "Statistical_report"
                        ],
                        "values": [
                                [v[0][0]]
                        ]
                }
        ]
}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6f7bccf6-607f-4ac4-9ab3-faa25e15cca6/predictions?version=2022-11-15', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    predictions=response_scoring.json()
    pred=predictions['predictions'][0]['values'][0][0]

    if(pred==1): 
        pred="Your are safe!! This is a Legitimate Website."
    else:
        pred="You are on the wrong site. Be cautious!" 
    
    return render_template("predict.html", prediction_text = '{}'.format(pred),url=url)

@app.route('/predict_api', methods=['POST'])
def predict_api():
    output=prediction[0]
    output.reshape(-1, 1)
    return jsonify(output)  


    
    

 

if __name__ == '__main__':
    app.run()


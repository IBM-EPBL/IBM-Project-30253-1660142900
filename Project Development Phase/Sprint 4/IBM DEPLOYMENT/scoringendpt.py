import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "OE-QJR_dqYubToiS8a2z_bokArc9V_t10jO1Pf0pja46"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {
        "input_data": [
                {
                        "fields": [
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
                                [
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1,
                                        1
                                ]
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
    print("Your are safe!! This is a Legitimate Website.")
else:
    print("You are on the wrong site. Be cautious!")


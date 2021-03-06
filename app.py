# Digital OCEAN FLASK SERVER RECEIVES IMAGE
from flask import Flask, request, jsonify
import classify
import base64
import firebase
import env
import json

# Instantiate Flask
app = Flask(__name__)


# health check
@app.route('/status')
def health_check():
    return 'Running!'


# Performing image Recognition on Image, sent as bytes via POST payload
@app.route('/detect', methods=["POST"])
def detect():

    imgBytes = request.data

    imgdata = base64.b64decode(imgBytes)
    with open("temp.png", 'wb') as f:
        f.write(imgdata)

    print("successfully receieved image")
    
    # Pass image bytes to classifier\
    imgPath= "testing.png"
    result = classify.analyse(imgPath)

    # Return results as neat JSON object, using 
    result = jsonify(result)
    print(result.json)

    response_data = result
    print(response_data)

    db = firebase.Firebase()
    db.authenticate()
    db.push(response_data)
    print("Updated Firebase.")

    return result

if __name__ == '__main__':
    app.run(host='127.0.1.1', port=6969, debug=True)

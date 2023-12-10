from flask import Flask,jsonify,request
import mediapipe_api
import converse_api

app = Flask(__name__)
MEDIAPIPE_API = mediapipe_api.MediaPipeAPI()
CONVERSE_API = converse_api.ConverseAPI()

@app.route('/')
def home():
    return 'API is up!!'

@app.route('/get-score',methods = ['POST'])
def sendScorePOST():
    text = request.get_json()['text']
    return jsonify(MEDIAPIPE_API.getScore(text))

@app.route('/get-score/<text>',methods = ['GET'])
def sendScoreGET(text):
    return jsonify(MEDIAPIPE_API.getScore(text))

@app.route('/get-response', methods = ['POST'])
def sendResponsePOST():
    text = request.get_json()['prompt']
    return jsonify(CONVERSE_API.getResponse(text))

@app.route('/get-response/<text>', methods = ['GET'])
def sendResponseGET(text):
    return jsonify(CONVERSE_API.getResponse(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 10000)

from flask import Flask,jsonify,request
import mediapipe_api

app = Flask(__name__)
API = mediapipe_api.MediaPipeAPI()

@app.route('/')
def home():
    return 'API is up!!'

@app.route('/get-score',methods = ['POST'])
def sendScorePOST():
    text = request.get_json()['text']
    return jsonify(API.getScore(text))

@app.route('/get-score/<text>',methods = ['GET'])
def sendScoreGET(text):
    return jsonify(API.getScore(text))

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
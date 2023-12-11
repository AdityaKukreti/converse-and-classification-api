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
    text = request.get_json()['prompt']
    return jsonify(MEDIAPIPE_API.getScore(text))

@app.route('/get-score/<prompt>',methods = ['GET'])
def sendScoreGET(prompt):
    return jsonify(MEDIAPIPE_API.getScore(prompt))

@app.route('/get-response', methods = ['POST'])
def sendResponsePOST():
    text = request.get_json()['prompt']
    return jsonify(CONVERSE_API.getResponse(text))

@app.route('/get-response/<prompt>', methods = ['GET'])
def sendResponseGET(prompt):
    return jsonify(CONVERSE_API.getResponse(prompt))

@app.route('/get-response-and-score', methods = ['POST'])
def sendResponseAndScorePOST():
    text = request.get_json()['prompt']
    score = MEDIAPIPE_API.getScore(text)
    return {'response':CONVERSE_API.getResponse(text)['response'],'category':score['category'],'score':score['score']}

@app.route('/get-response-and-score/<prompt>', methods = ['GET'])
def sendResponseAndScoreGET(prompt):
    score = MEDIAPIPE_API.getScore(prompt)
    return jsonify({'response':CONVERSE_API.getResponse(prompt)['response'],'category':score['category'],'score':score['score']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 10000)

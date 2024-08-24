from dotenv import load_dotenv
from googletrans import Translator
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import markdown2 as md2
import os

from summarizedText import generate_gemini_content
from url_to_textfunction import extract_transcript_details
from transcribeAudio import transcribe_telugu_audio

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

url = ""
transcript = ""
video_id = ""

# Define the resource for handling POST and GET requests
class URLHandler(Resource):
    def post(self):
        global url, transcript, video_id
        data = request.get_json()  # Get the JSON data sent in the POST request
        url = data.get('url', '')  # Extract the 'text' field from the JSON

        # print('url', url)
        resp = extract_transcript_details(url)
        # print(resp)
        transcript = resp['transcript']
        video_id = resp['video_id']

        # print('transcript', transcript)

        return {"message": "URL received", "received_url": url}, 201

    def get(self):
        global transcript, video_id
        # print('I GOT THE TRANSCRIPT: ', transcript[:20])
        resp = generate_gemini_content(transcript)
        summary = md2.markdown(resp)
        return {"summary": summary, "video_id": video_id}, 200
    

class FileHandler(Resource):
    def post(self):
        if 'file' not in request.files:
            return jsonify({"message": "No file part"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        if file:
            filename = 'audio1'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('uploaded')
            response = jsonify({"message": "File uploaded successfully", "filename": filename})
            response.status_code = 200
            return response
    
    def get(self):
        return jsonify({"message": "This URL does not have a GET handler. Please try POST only"})
    
class LocalSummary(Resource):
    def get(self):
        transcript = transcribe_telugu_audio('uploads/audio1')
        return jsonify({"summary": transcript})

# Add the resource to the API with a specific endpoint
api.add_resource(URLHandler, '/URLsummary')
api.add_resource(FileHandler, '/uploadFile')
api.add_resource(LocalSummary, '/localSummary')

if __name__ == '__main__':
    app.run(debug=True)

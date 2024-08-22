from dotenv import load_dotenv
from googletrans import Translator
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import markdown2 as md2

from summarizedText import generate_gemini_content
from url_to_textfunction import extract_transcript_details

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

url = ""
transcript = ""

# Define the resource for handling POST and GET requests
class TextHandler(Resource):
    def post(self):
        global url
        global transcript
        data = request.get_json()  # Get the JSON data sent in the POST request
        url = data.get('url', '')  # Extract the 'text' field from the JSON

        # print('url', url)

        transcript = extract_transcript_details(url)
        # print('transcript', transcript)

        return {"message": "URL received", "received_url": url}, 201

    def get(self):
        global transcript
        print('I GOT THE TRANSCRIPT: ', transcript[:20])
        resp = generate_gemini_content(transcript)
        summary = md2.markdown(resp)
        return {"summary": summary}, 200

# Add the resource to the API with a specific endpoint
api.add_resource(TextHandler, '/URLsummary')

if __name__ == '__main__':
    app.run(debug=True)

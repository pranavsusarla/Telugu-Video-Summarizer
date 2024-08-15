import streamlit as st
from dotenv import load_dotenv
from googletrans import Translator  # Import the Translator class

load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

# Initialize the translator
translator = Translator()

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

def translate_to_telugu(text):
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Summarize"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        telugu_summary = translate_to_telugu(summary)

        # Create tabs for English and Telugu summaries
        tab1, tab2 = st.tabs(["English Summary", "Telugu Summary"])

        with tab1:
            st.markdown("## Detailed Notes in English:")
            st.write(summary)

        with tab2:
            st.markdown("## Detailed Notes in Telugu:")
            st.write(telugu_summary)

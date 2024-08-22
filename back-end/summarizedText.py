#fuction which takes text from the vedio transcripts and summarizes the text
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_gemini_content(transcript_text):

    if transcript_text=='':
        return 'Transcript is empty !!'

    prompt = """You are a YouTube video summarizer. You will be taking the transcript text
    and summarizing the entire video and providing the important summary in points
    within 250 words. Provide summmary in the form of bullet points ONLY. REMEMBER THIS INSTRUCTION. THE SUMMARY SHOULD BE IN ENGLISH ONLY. Please provide the summary of the text given here:  """   

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

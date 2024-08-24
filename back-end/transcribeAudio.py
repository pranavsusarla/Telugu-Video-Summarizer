# import whisper

def transcribe_telugu_audio(file_path):
    # Load the Whisper model
    model = whisper.load_model("base")  # You can choose different model sizes like "tiny", "base", "small", "medium", "large"
    
    # Transcribe the audio file
    result = model.transcribe(file_path, language="te")  # 'te' is the language code for Telugu
    
    # Get the transcription text
    transcription = result["text"]
    
    return transcription

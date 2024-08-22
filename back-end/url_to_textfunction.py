from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'te'])

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        

        return {
            'transcript': transcript,
            'video_id': video_id
        }

    except Exception as e:
        raise e

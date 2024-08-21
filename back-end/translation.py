#function of translation English to Telugu 

def translate_to_telugu(text):
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

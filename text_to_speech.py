from gtts import gTTS

# Docs for mores Language and accents https://gtts.readthedocs.io/en/latest/module.html#localized-accents
def text_to_speech(text, language='es', tld='com.mx'):
    tts = gTTS(text=text,tld=tld, lang=language, slow=False,)
    return tts

def save_audio(tts, filename='output.mp3'):
    tts.save(filename)


text_to_convert = "This is an audio test"

tts = text_to_speech(text_to_convert)
save_audio(tts)
print("Audio created! 🎉")

# Made by https://github.com/HenFray

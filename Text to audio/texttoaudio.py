import gtts ,playsound
audio="speech.mp3"
language='en'
sp=gtts.gTTS(text=input(),lang=language,slow=False)
sp.save(audio)
playsound.playsound(audio)
# print("===audio is play====")
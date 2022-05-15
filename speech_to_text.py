import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    user=""
    with sr.Microphone()as source:
        print("Listening")
        r.pause_threshold = 1
        audio =r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing")
        user =r.recognize_google(audio,language= 'en-pk')
        return user

    except Exception as e:
         user= "you have not said any thing......... "
         return user
    return user
text = takecommand()
print(text)

import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("Voices", voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

speak("Hellow Dear how are you?")
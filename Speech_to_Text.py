# Import the pyttsx3 module for text-to-speech and the speech_recognition module for speech recognition.
import pyttsx3
import pyttsx3
import speech_recognition as sr

def get():
    r = sr.Recognizer()                      # Instance of recoganizer Class from speech recognition module.
    with sr.Microphone() as source:          # audio source (the user's microphone)/
        print("say Something...!")
        audio = r.listen(source)             # Capture the audio from the microphone.
        print( "Done!")

    try:
        text = r.recognize_google(audio)     # Use the recognize_google() to recognize the speech.

        print("you Said: " + text)
    except Exception as e:
        print(e)

get() 
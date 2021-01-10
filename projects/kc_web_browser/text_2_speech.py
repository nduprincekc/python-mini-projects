import pyttsx3

def speak(kc):
    kc = input()
    engine = pyttsx3.init()
    engine.say(kc)
    engine.runAndWait()

speak('ok')

e = pyttsx3.init()
voices = e


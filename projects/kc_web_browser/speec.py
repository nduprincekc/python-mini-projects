import speech_recognition as sr
def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio = r.listen(source)
take()

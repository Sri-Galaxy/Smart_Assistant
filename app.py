import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

recog = sr.Recognizer()
engine = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello Sri I am Asher!")

    while True:
        r = sr.Recognizer()

        print("Recognising the word...")
        try:
            with sr.Microphone() as source:
                print("Say something..!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)

            if(word.lower() == "asher"):
                speak("Jo hukum mere aaka..!")

                with sr.Microphone() as source:
                    print("Asher Active..!")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)
        except Exception as e:
            print(e)



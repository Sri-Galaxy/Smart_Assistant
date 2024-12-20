import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

engine  = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("This is Asher")

    while True:
        r = sr.Recognizer()
        
        print("Recognising...")
        try:
            with sr.Microphone() as source:
                print("Say Something..!")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print(f"Error: {e}")



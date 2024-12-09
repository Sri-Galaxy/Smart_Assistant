import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

engine = tts.init()

def res(text):
    engine.say(text)
    engine.runAndWait()


def req(c):
    if "open google" in c:
        wb.open("https://google.com")
    elif "open youtube" in c:
        wb.open("https://youtube.com")


if __name__ == "__main__":
    res("Hello Sri I am Asher!")

    while True:
        r = sr.Recognizer()

        print("Recognising the word...")
        try:
            with sr.Microphone() as source:
                print("Say something..!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)

            if(word.lower() == "asher"):
                res("Yes Boss")

                with sr.Microphone() as source:
                    print("Asher Active..!")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    req(command.lower())

        except Exception as e:
            print(f"ERROR: {e}")



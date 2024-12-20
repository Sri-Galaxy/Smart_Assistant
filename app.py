import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

engine  = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        wb.open("https://google.com")
    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")
    else:
        pass
        

if __name__ == "__main__":
    speak("----------This is Jarvis!----------")
    print("----------This is Jarvis!----------")

    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("\nSay Something..!\n")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis"):
                print("Yes Boss..\n")
                speak("Yes Boss!")
                
                with sr.Microphone() as source:
                    print("Jarvis is Active..!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    
        except Exception as e:
            print(f"Error: {e}")



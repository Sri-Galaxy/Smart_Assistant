import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
import my_model as gm
engine  = tts.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google.com")
        wb.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        wb.open("https://youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        wb.open("https://instagram.com")
    elif "shutdown" in c.lower():
        speak("Thank you for the day.")
        exit(0)
    else:
        speak("Hmm, let me think...")
        reply = gm.gemini_response(c)
        speak(reply)



if __name__ == "__main__":
    speak("This is Jarvis!")

    while True:
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("\nUnder your Command Sir...!\n")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis"):
                speak("Yes Boss!")
                
                with sr.Microphone() as source:
                    print("Jarvis is Active..!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
                    
        except Exception as e:
            print(f"Error: {e}")



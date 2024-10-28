import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
        print("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
        print("Good afternoon!")
    else:
        speak("Good evening!")
        print("Good evening!")

def get_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    return time

def get_date():
    date = datetime.datetime.now().strftime('%B %d, %Y')
    return date

def open_chrome():
    webbrowser.open(f"https://www.google.com")
    
def open_spotify():
    programName = "C:\\Users\\ACER\\AppData\\Roaming\\Spotify\\Spotify.exe"
    subprocess.Popen([programName])
    
def open_youtube():
    webbrowser.open(f"https://www.youtube.com")
    
def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen_command()
        if 'hello' in command:
            greet()
        elif 'time' in command:
            current_time = get_time()
            speak(f"The time is {current_time}")
        elif 'date' in command:
            current_date = get_date()
            speak(f"Today's date is {current_date}")
        elif 'spotify' in command:
            open_spotify()
            speak("Opening Spotify")
        elif 'chrome' in command:
            open_chrome()
            speak("Opening Google Chrome")
        elif 'search' in command:
            query = command.replace("search", "").strip()
            speak(f"Searching for {query}")
            search_web(query)
            print("Searching for {query}")
        elif 'youtube' in command:
            open_youtube()
            speak("opening youtube!")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

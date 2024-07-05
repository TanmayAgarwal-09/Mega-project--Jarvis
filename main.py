import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="31cb9bcedbcf40da8065d07b0741c6f0"
def processCommand(c):
    print(c)
    if "open goggle" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=31cb9bcedbcf40da8065d07b0741c6f0")
        if r.status_code ==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles:
                speak(article['title'])


def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak("Initialising jarvis...")
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
       

        print("Recognizing....")
# recognize speech using Sphinx
        try:
             with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
             word=r.recognize_google(audio)
             if word.lower()=="jarvis":
                 speak("yes")
                #Listen for command
                 with sr.Microphone() as source:
                    print("jarvis active!")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                 command=r.recognize_google(audio)
                 processCommand(command)

                 
        except Exception as e:
             print("Error;{0}".format(e))
 

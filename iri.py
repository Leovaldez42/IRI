import datetime
import os.path
from instagram import Instagram
import random
import smtplib
import sys
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('')
voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice)
# print(voices[11].id)
engine.setProperty('voice', 'english')  # 11 is for english

emails = {
    'name': 'email@gmail.com'

}
movies = {
    'action': 0,
    'adventure': 1,
    'animation': 2,
    'biography': 3,
    'comedy': 4,
    'crime': 5,
    'documentary': 6,
    'drama': 7,
    'family': 8,
    'fantasy': 9,
    'film-noir': 10,
    'game-show': 11,
    'history': 12,
    'horror': 13,
    'music': 14,
    'musical': 15,
    'mystery': 16,
    'news': 17,
    'reality': 18,
    'romance': 19,
    'sci': 20,
    'sitcom': 21,
    'sport': 22,
    'talk-show': 23,
    'thriller': 24,
    'war': 25,
    'western': 26
}
how_are_you = {
    1: 'Thank you for asking, I am well. How can I help you',
    2: 'Your voice literally perks me up, how are you',
    3: 'I have had an exciting day looking for fun things to do, how may I help you',
    4: 'I am wonderful, how may I help'
}
girlfriend = {
    1: 'I\'m all for setting dates and chatting with you',
    2: 'I\'m here whenever you need a assistant',
    3: 'Sorry I am committed to my work.I am sure out of the 7.2 billion people on Earth there is someone '
       'for you, what about Aditi?'
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 8:
        speak("Hello Gaurav, Good morning. You are working quite early today.")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")
    elif 8 <= hour <= 12:
        speak("Hello Gaurav, Good morning")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")
    elif 12 <= hour < 18:
        speak("Hello Gaurav, good afternoon, nice to have you back")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")
    elif 18 <= hour <= 22:
        speak("Hello Gaurav, Good Evening, nice to have you back")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")
    else:
        speak("Hello Gaurav, Good gracious you are working quite late sir")
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {strTime}")

    speak("Please tell me how may I help you.")


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your_password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


def take_command():
    # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening.... ")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, phrase_time_limit=5)
        except Exception as e:
            print(e)

    try:
        print("Recognizing.... ")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        # Logic for executing task
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            # print(results)
            speak(results)
        elif 'hello' in query:
            speak("Hi sir")
        elif 'how are you' in query:
            # Go to dictionary how_are_you to check commands
            speak(how_are_you.get(random.randint(1, len(how_are_you))))
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'open instagram' in query:
            speak("Opening instagram")
            webbrowser.open("https://www.instagram.com/")
        elif 'movie' in query:
            speak("Which type of movie would you like to watch sir.")
            genre = input("Enter movie type: ").lower()
            if genre in movies:
                string = "https://moviegaga.to/suggest-me?t=0&g=" + str(movies.get(genre))
                webbrowser.open(string)
            else:
                webbrowser.open('https://moviegaga.to')
        elif 'open google' in query:
            speak("Want to search something sir?")
            speak("Opening google.com")
            webbrowser.open("https://www.google.com/")
        elif 'open stackoverflow' in query:
            speak("Have a coding doubt sir?")
            speak("Opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")
        elif 'open gmail' in query:
            speak("Good time to check some email.")
            speak("Opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")
        elif 'open codechef' in query:
            speak("Feeling like coding sir great")
            webbrowser.open("https://www.codechef.com/")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open code' in query:
            speak("Opening VS code")
            os.system('code')
        elif 'open sublime' in query:
            speak("Opening sublime text")
            os.system('sublime-text.subl')
        elif 'open pycharm' in query:
            speak("Opening Pycharm-Profession")
            os.system('pycharm-professional')
        # # elif 'face' in query:
        # #     os.system('pass')
        elif 'send email' in query:
            try:
                speak("Whom do you want to send the email to")
                person = input("Name of the person").lower()
                speak("What do you want to say")
                content = input("Enter the message: ")
                to = emails.get(person)
                send_email(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send the email")
        elif 'bye' in query or 'sleep' in query:
            speak("Bye Sir, have a great day ahead")
            sys.exit()
        elif 'girlfriend' in query:
            speak("Concentrate on studies Gaurav and as regarding girlfriend")
            speak(girlfriend.get(random.randint(1, len(girlfriend))))
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop iri from listening commands")
            a = int(take_command())
            print(a)
            time.sleep(a)
            print(a)
        elif 'shutdown' in query:
            shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
            if shutdown == 'no':
                exit()
            else:
                os.system("shutdown /s /t 1")
        elif 'restart' in query:
            check = input("Want to restart your computer ? (y/n): ")
            if check == 'n':
                exit()
            else:
                os.system("shutdown /r /t 1")
        elif 'check instagram' in query:
            Instagram()
        elif 'bored' in query:
            os.system('Alien_invasion/alien_invasion.py')

        elif 'google it' in query or 'search' in query or 'what is' in query:
            print(query)
            answer = take_command().lower()
            if 'yes' in answer or 'yeah' in answer or 'yup' or 'thrill me' in answer:
                string = str("https://www.google.com/search?q =" + '+'.join(str(query)))
                print(string)
                webbrowser.open(string)
            else:
                pass

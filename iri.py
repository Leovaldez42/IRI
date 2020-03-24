import datetime
import os.path
import random
import smtplib
import sys
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
from instagram import Instagram

engine = pyttsx3.init()
voices = engine.getProperty('voices')
client = wolframalpha.Client('your-wolfram-id')

# for voice in voices:
#     print(voice)
# print(voices[11].id)
engine.setProperty('voice', 'english')

emails = {
    'myself': 'youremail@abcd.com',
    'your_friend': 'his_email@abcd.com'

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
    4: 'I am wonderful, how may I help',
    5: "I'm fine, thank you, what can I do for you",
    6: "Good to hear from you! How may I help",
    7: "Today has been inspiring. We can learn a lot of new things, how may I help"
}
girlfriend = {
    1: 'I\'m all for setting dates and chatting with you',
    2: 'I\'m here whenever you need a assistant',
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 8:
        speak("Hello Gaurav, Good morning. You are working quite early today.")
        time_now = datetime.datetime.now().strftime('%H:%M')
        speak(f"Sir the time is {time_now}")
    elif 8 <= hour <= 12:
        speak("Hello Gaurav, Good morning")
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {time_now}")
    elif 12 <= hour < 18:
        speak("Hello Gaurav, good afternoon, nice to have you back")
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {time_now}")
    elif 18 <= hour <= 22:
        speak("Hello Gaurav, Good Evening, nice to have you back")
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {time_now}")
    else:
        speak("Hello Gaurav, Good gracious you are working quite late sir")
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir the time is {time_now}")

    speak("Please tell me how may I help you.")


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@abcd.com", "yourpassword")
    server.sendmail("youremail@abcd.com", to, content)
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
        elif 'open wolfram alpha' in query:
            speak("Opening wolfram alpha")
            webbrowser.open('https://www.wolframalpha.com/')
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
        elif 'bored' in query or 'game' in query:
            speak("Feeling bored sir, let's play a game")
            os.system('python IRI/alien-invasion/game.py')

        else:
            speak("Do you want me to search " + query)
            answer = take_command()
            if "yes" in answer or "yup" in answer or "thrill me" in answer:

                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('WOLFRAM-ALPHA says - ')
                        speak('Got it.')
                        speak(results)
                        print(results)

                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
                        print(results)

                except:
                    webbrowser.open('https://www.google.com/')
            else:
                speak("Okay I won't search that")

# IRI

A virtual assistant that would be able to do a wide variety of things.

## Getting Started

Click the clone button and open it using a text editor (preferably Pycharm or VS code)

### Prerequisites

Make sure you have Python 3.6 or newer installed on your PC. To check if python is installed in your PC, open 
termainal and write python. In case you don't get error you are good to go, otherwise install python on your device.


### Installing


## Deployment

### Voices
Linux users : Use this as it is, although you might want to change language based on your preference.
              To do that uncomment the 15 and 16 and checks out the list of voices, and replace 'english' with the                   voice id. If you would like the voice to be a little girl like, you can use 'voice-id+f(1,2,3,4)'. Any                 one of the numbers, but it shall increase the echo of the voice. Eg 'english+f4'.Higher the number, more               the voice will be girl like and more echo.
              
Windows users : For windows, your voice shall be more human like. You need to use 'sapi5'
So replace line 12 with
```
engine = pyttsx3.init('sapi5')
```
and line 18 with
```
engine.setProperty('voice', voices[0].id)     # 0 for male and 1 for female.
```

### Emails
This is a dictionary so you just write 
'name' : 'his_email@abcd.com'
You can make a list the people whom you want to send email to

### Movies
I have used movieninja.io for it to open movies, however you can connect it with any website as you wish. Details 
shall be given furthur.

### how_are_you
This are a bunch of statements it shall use to wish me, you can add or remove as you wish.

### Speak
Don't change this.

### wish_me
You can replace this however you want, this is just the way I liked.

### send_email
In this you need to do a few steps.
1) Make sure you have a gmail account
2) Go to your Google account and click on security.
3) Scroll a bit down and allow less secure apps
4) Now you are all set

replace ' ' on line 96 with your email id and password of your gmail.
replace ' ' on line 97 with your email id.

### take_command
You can change the phase_time_limit as per your convenience
On line 115 
```
query = r.recognize_google(audio)
```
you can replace google with another search_engine

### main_methord 
You can edit this as per your convenience
In the send email, you can decide to speak the content of letters too snd also whom you want to send it.
Just check the above few commands and you shall get the hang of it.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.



## Authors

* **Gaurav Sharma** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

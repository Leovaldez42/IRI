# IRI

A virtual assistant to do daily tasks

## Getting Started

Click the clone repository button. Follow the prerequisites and run
```
pip install -r requirements.txt
```

to install all the packages required.

### Prerequisites

Make sure you have python 3.6 or higher installed on your device. To check 
python version on your device type

```
python
```
If it does not give any error it means python is installed on your device
and you can also check the version.

Also run the following commands on terminal/ powershell
```
pip install --upgrade pip
pip install pywin32
```
## Deployment

For linux users: You can use the voice commands printed on line 13-18 as it is. In case you want to change the voice
uncomment the lines 18-19 as
```
for voice in voices:
    print(voice)
```
and choose the voice you require. Then replace 'english' with the voice id.

For windows users: Replace line 14 with
```
engine = pyttsx3.init('sapi5')
```
and line 21 with
```
engine.setProperty('voice', voices[0].id)   # Replace 0 with 1 for female voice
```
### Client
1) Go to https://www.wolframalpha.com
2) Sign in, in case you do not have account sign up.
3) On the right most corner click your account and head over to My Apps(API)
4) Click get an APP-ID and fill the required information and get an app-id
5) Replace your-wolfram-id with your app-id

### emails
This shall be used to send emails through the voice command. To use it
type the name of the person and his/her email id as per the format.

### movies
I have used movieninja.io to open movies, you can change it as per your convenience.

### how_are_you and girlfriend
You can change the sentences as you wish.

### wish_me
You can change this as per your convenience. 

### Using send email 
1) If you do not have google account create one.
2) Open your gmail account and go to manage your google account, Security.
3) Scroll down and allow less secure apps.
4) On line 102 replace "youremail@gmail.com" with your gmail id and "your_password" with its password
5) On line 103 replace "youremail@gmail.com" with your email id.

### take_command
You can adjust phrase_time_limit as per your convenience.

### main
You can adjust various commands as you wish, follow the below mention things.
1) In case of opening vs-code and sublime on windows open file location 
of them, click on properties and copy the target and replace it with 'code'. 
Whereever there is \ make it \\. Do the same for all.
#####using send email
1) say send email
2) using the list of emails, type the name to whom you want to send email to.
3) Type the content of email.
4) Click enter.
5) Email would have been sent.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Leovaldez42/IRI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

1.0.5

## Authors

* **Gaurav Sharma** 

## License

This project is licensed under the MIT License - see the [LICENSE.](LICENSE) file for details


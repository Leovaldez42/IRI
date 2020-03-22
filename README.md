# IRI

A virtual assistant to do daily tasks

## Getting Started

Click the clone repository button and type 
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
uncomment the lines 15-16 as
```
for voice in voices:
    print(voice)
```
and choose the voice you require. Then replace 'english' with the voice id.

For windows users: Replace line 13 with
```
engine = pyttsx3.init('sapi5')
```
and line 18 with
```
engine.setProperty('voice', voices[0].id)   # Replace 0 with 1 for female voice
```

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

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning


## Authors

* **Gaurav Sharma** 

## License

This project is licensed under the MIT License - see the [LICENSE.](LICENSE) file for details


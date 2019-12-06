# botTranslator_WithDiscord
An autonoumous bot translator can be integrated with discord platform.
![Demo](https://github.com/Ridha-ELGHOUL/botTranslator_WithDiscord/blob/master/img/demo_bot.png)
# Requirements
##### Python version: python3.x. (download: https://www.python.org/downloads/)
##### Package to install: 
``` 
pip install discord  
            speech_recognition
            googletrans
            pyttsx3
            gTTS
```
# Configuration and integration
you need to create:
- Discord account to add your bot and test its functionalities and interacte with (https://discordapp.com/). 
- An application that your bot will use to authenticate with Discord’s APIs (to get token and id used later in your bot app).
to create your bot app, follow this link: https://discordapp.com/developers/applications
![Demo](https://github.com/Ridha-ELGHOUL/botTranslator_WithDiscord/blob/master/img/create_app.png)
- A bot user that you’ll use to interact with other users and events in your guild
![Demo](https://github.com/Ridha-ELGHOUL/botTranslator_WithDiscord/blob/master/img/bot_app.PNG)
- A guild in which your user account and your bot user will be active
# Start and test your app
```
python bot.py
```
# Next work !
- Customize better bot app.
- Add voice translation integrated to discord.
- Choose your language (Source language): to be detected automatically from the sys language.

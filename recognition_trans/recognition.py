import speech_recognition as sr
from googletrans import Translator
import pyttsx3
from gtts import gTTS

def RecognitionToText(lang=None,lang_des='en'):
    #instance of recognizer class
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("RECOGNITON STARTED ... Tell something");
        print ("---------------- Recording  -----------");
        audio = r.listen(source)
        print ("FINISH RECORDING ... ")

    # Speech recognition using Google Speech Recognition
    try:
        if lang == None :
            print ("**********************Auto Detection*****************");
            #ldetec = 
            text_recognitized = r.recognize_google(audio)
        else:
            text_recognitized = r.recognize_google(audio, language = lang)

        print ("********************************************");
        print("YOU SAID : ")
        print( text_recognitized)
        print ("********************************************");
        LanguageDetect(text_recognitized)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def LanguageDetect(text):
    translator = Translator()
    detected_lang = translator.detect(text)
    lang_des = detected_lang.lang
    if lang_des !='en':
        trans= str(translator.translate(text,dest='en'))
    else:
        trans= str(translator.translate(text,dest='de'))
    transText = trans.split(",")
    #print ("********************************************");
    #print ("TRADUCTION :  "+ transText[2][6:])
    #print ("********************************************");
    #TextTospeech(transText[2][6:])
    return  transText[2][6:]
def TextTospeech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 
    #engine.setProperty('voice',voice.language
    engine.say(text)
    engine.runAndWait()
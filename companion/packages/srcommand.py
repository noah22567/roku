from gtts import gTTS
import speech_recognition as sr
import os
import re
import smtplib
import requests
import json


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    "listens for commands"

    capture = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        capture.pause_threshold = 1
        capture.adjust_for_ambient_noise(source, duration=1)
        audio = capture.listen(source)

    try:
        command = capture.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command



import speech_recognition as sr
import pandas as pd


def myCommand():
    "listens for commands"

    capture = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        capture.pause_threshold = 2
        # capture.adjust_for_ambient_noise(source, duration=1)
        audio = capture.listen(source)

    try:
        command = capture.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        if command:
            try:
                command_split = command.split(" ")
                command_phrase = command_split[command_split.index("command")+1:command_split.index("action")]
                command_action = command_split[command_split.index("action")+1:]
                ord_phrase = WordToOrd(command_phrase)
                ord_action = WordToOrd(command_action)
                phrase = listToString(command_phrase)
                action = listToString(command_action)
                print("Phrase: ", command_phrase)
                print("----"*30)
                print("Action: ", command_action)
                data = pd.DataFrame({'phrase': [phrase],"action":[action],"ord_phrase":[ord_phrase], "ord_action": [ord_action]})

                import os
                # if file does not exist write header
                if not os.path.isfile('commandData.csv'):
                    data.to_csv('commandData.csv', header=['phrase',"action","ord_phrase","ord_action"])
                else:  # else it exists so append without writing the header
                    data.to_csv('commandData.csv', mode='a', header=False)
                print("successfully collected data")
                print(data)
            except:
                print("failed to collect")
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()

    return command

def WordToOrd(word_list):
    word_ord = ""
    for word in word_list:
        for letter in word:
            word_ord += str(ord(letter))
        return word_ord


def get_verb(phrase):
    phrase_list = []
    verb_list = ["play","stop","go","select","pause","forward","back","left","right","power","on"]
    for word in phrase:
        if word in verb_list:
            phrase_list.append(word)
    if phrase_list == []:
        raise ValueError("Action missing from verb list")
    return phrase_list


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


while True:
    myCommand()


from bs4 import BeautifulSoup
from requests import Session
import json
import pandas as pd
import os


# return [defintions]
def WordClean(word):
    data = word.strip("][")
    data = word.replace('"', "")
    data = word.replace("'", "")
    data = word.replace(",", "")
    data = data.replace(";", "")
    data = data.replace("\t", "")
    data = data.replace("\n", "")
    word = data.replace(" ", "")

    return word


def Get_Def(word):
    print("Looking for data on {}".format(word))
    ses = Session()
    req = ses.get("https://www.thesaurus.com/browse/{search_word}?s=t".format(search_word=word))
    text = req.text
    soup = BeautifulSoup(text, 'html.parser')
    som = str(soup.find_all("script")[22]).strip("<script> window.INITIAL_STATE = ").strip(";</")
    search_data = json.loads(som)['searchData']['tunaApiData']['posTabs']
    print("search data: ", search_data)
    definitions = []
    for phrase in search_data:
        try:
            preproc = phrase['definition']
            if ";" in preproc or "," in preproc:
                preproc = preproc.replace(";", ",").split(",")
            definitions = preproc
        except:
            continue
    if not definitions:
        print("Failed to find data on {}".format(word))
    print("definitions extracted", definitions)
    return definitions


def ProccessData(file):
    # definitions = []
    word = []
    if "txt" in file:
        print("Attempting to process {}:".format(file))
        os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist/new/")
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    words_list = line.split(" ")
                    word = WordClean(words_list.pop())
                    definitions = Get_Def(word)

                    if definitions:
                        if type(definitions) == list:
                            definitions.append(word)
                            print("Succesfully downloaded synonyms for {}".format(word))
                            MakeData(definitions)
                        else:
                            print("Succesfully downloaded synonyms for {}".format(word))
                            definitions = [definitions, word]
                            MakeData(definitions)
                except:
                    print("Failed to get definition.")

    elif "csv" in file:
        print("Attempting to process {}:".format(file))
        os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw/")
        df = pd.read_csv(file)
        df = df['phrases']
        for line in df:
            try:
                words_list = line.split(" ")
                for word in words_list:
                    word = WordClean(word)
                    definitions = Get_Def(word)
                    if definitions:
                        if type(definitions) == list:
                            definitions.append(word)
                            print("Succesfully downloaded synonyms for {}".format(word))
                            MakeData(definitions)
                        else:
                            print("Succesfully downloaded synonyms for {}".format(word))
                            definitions = [definitions, word]
                            MakeData(definitions)
            except:
                print("Failed to get definition.")
    else:
        print("Wrong file type")




def CleanCSVData():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw")
    list_dir = os.listdir(os.getcwd())
    for filename in list_dir:
        if ".csv" in filename:
            df = pd.read_csv(os.getcwd() + "/" + filename)
            phrases = df['phrases']
            phrases = phrases.drop_duplicates()
            phrases.to_csv("/home/noah/Desktop/Funstuff/ml/data/collection/clean/clean" + filename, mode="w",
                           header=True)



def GetName():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    if listdir == []:
        return "1.csv"
    else:
        last_name = str(max(flist)) + ".csv"
        df = pd.read_csv(os.getcwd() + "//" + last_name)
        if len(df['phrases']) > 50000:
            new_name = str(max(flist) + 1) + ".csv"
            return new_name
        else:
            return last_name


def GetRecentName():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    if listdir == []:
        return "1.csv"
    return str(max(flist)) + ".csv"


def MakeData(words):
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw")
    name = GetName()
    try:
        if name in os.listdir(os.getcwd()):
            pd.DataFrame({"phrases": [words]}).to_csv(name, mode='a', header=False)
            print("Succefully stored new values to {name}".format(name=name))
        else:
            pd.DataFrame({"phrases": [words]}).to_csv(name, mode='w', header=True)
            print("Succefully stored new values to {name}".format(name=name))
    except:
        print("Failed to store data on {word}".format(word=words))

def MoreWords():
    print("Starting MoreWords!")
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist/new/")
    list_dir = os.listdir(os.getcwd())
    for file in list_dir:
        ProccessData(file)

    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/raw/")
    list_dir = os.listdir(os.getcwd())
    for file in list_dir:
        ProccessData(file)
    CleanCSVData()

MoreWords()

from bs4 import BeautifulSoup
from requests import Session
import json
import pandas as pd
import os

def GetDef(word):
    ses = Session()
    req = ses.get("https://www.thesaurus.com/browse/{search_word}?s=t".format(search_word = word))
    text = req.text
    soup = BeautifulSoup(text, 'html.parser')
    som = str(soup.find_all("script")[22]).strip("<script> window.INITIAL_STATE = ").strip(";</")
    search_data = json.loads(som)['searchData']['tunaApiData']['posTabs']

    defintions = []
    for ting in search_data:
        preproc = ting['definition']
        if ";" in preproc or "," in preproc:
            preproc = preproc.replace(";", ",").split(",")
        defintions = preproc
    if defintions != []:
        if type(defintions) == list:
            defintions.append(word)
            print("Succesfully downloaded synonyms for {}".format(word))
            return defintions
        else:
            print("Succesfully downloaded synonyms for {}".format(word))
            return [defintions,word]


def MakeCollection(words, name):
    # words = '["synonyms":{}]'.format(words)
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    if name in os.listdir(os.getcwd()):
        pd.DataFrame({"phrases":[words]}).to_csv(name, mode='a', header=False)
        print("Succefully appended new values to {name}".format(name=name))
    else:
        pd.DataFrame({"phrases":[words]}).to_csv(name, mode='w', header=True)
        print("Succefully appended new values to {name}".format(name=name))


def CleanData(file):
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist/new")
    with open(file, "r") as file:
        print("Formatting data in file: {file}".format(file=file))
        data = file.read()
        data = data.replace(","," ")
        data = data.replace(";"," ")
        data = data.replace("\t"," ")
        data = data.replace("\n"," ")
        words = data.split(" ")
        print("Completed formatting.")
        return words



def GetName():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection/")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    if listdir == []:
        return "1.csv"
    else:
        last_name = str(max(flist))+".csv"
        df = pd.read_csv(os.getcwd()+"//"+last_name)
        if len(df['phrases']) > 50000:
            new_name = str(max(flist) + 1)+".csv"
            return new_name
        else:
            return last_name

def GetRecentName():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    if listdir == []:
        return "1.csv"
    return str(max(flist))+".csv"




## pull words from verbsync
# if its a phrase dont
#else continue

def MoreWords():
    import copy
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    current = GetRecentName()
    next_name = GetName()
    name = copy.deepcopy(next_name)

    for file in os.listdir(os.getcwd()):
        df = pd.read_csv("/home/noah/Desktop/Funstuff/ml/data/collection/" + current)

        # phrases = df[1]
        # for syn in phrases:
        #     this = syn.split(",")#or maybe json load it
        #     for ting in this:
        #         ting = ting.split(" ")
        #         if len(ting) == 1:
        #             wordslist = Get_Def(ting)
        #             make_collection(wordslist, name)
        #         name = next_name

# MoreWords()





## when comes time to clean if word is repeated and has a row where its alone remove the one that is alone
## else leave it
#


def Words():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist/new")
    listdir = os.listdir(os.getcwd())
    total = 0
    success_data = 0
    for file in listdir:
        if ".txt" in file:
            words_list = CleanData(file)
            total = len(words_list)
            print("Currently finding data using: {file}".format(file=GetRecentName()))
            if words_list != None:
                for word in words_list:
                    try:
                        defs = GetDef(word)
                        MakeCollection(defs, GetName())
                        success_data +=1
                    except:
                        print("Failed to get data on {word}".format(word=word))
                        continue
            z = (100/success_data+total)
            print("{file}\n".format(file=file))
            print("Percentage: ", str(success_data*total)+"%")

        z = (100/success_data+total)
        print("Overall percentage: ", str(success_data*total)+"%")

Words()

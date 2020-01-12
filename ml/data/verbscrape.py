from bs4 import BeautifulSoup
from requests import Session
import json
import pandas as pd
import os

def Get_Def(word):
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
            return defintions
        else:
            return [defintions]


def make_collection(words,name):
    # words = '["synonyms":{}]'.format(words)
    print(words)
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    pd.DataFrame({"phrases":[words]}).to_csv(name, mode='a', header=False)


def words():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist/new")
    listdir = os.listdir(os.getcwd())
    words = None
    for file in listdir:
        if ".txt" in file:
            with open(file, "r") as file:
                data = file.read()
                data = data.replace(","," ")
                data = data.replace(";"," ")
                data = data.replace("\t"," ")
                data = data.replace("\n"," ")
                words = data.split(" ")

    if words != None:
        for word in words:
            # print(word)
            try:
                defs = Get_Def(word)
                make_collection(defs)
            except:
                continue

def get_name():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    return str(max(flist)+1)+".csv"

def get_recent_name():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    listdir = os.listdir(os.getcwd())
    flist = []
    for file in listdir:
        flist.append(int(file.rstrip(".csv")))
    return str(max(flist))+".csv"





# words()

## pull words from verbsync
# if its a phrase dont
#else continue

def morewords():
    import copy
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/collection")
    current = get_recent_name()
    next_name = get_name()
    name = copy.deepcopy(next_name)

    for file in os.listdir(os.getcwd()):
        df = pd.read_csv("/home/noah/Desktop/Funstuff/ml/data/collection/" + current)
        phrases = df[1]
        for syn in phrases:
            this = syn.split(",")#or maybe json load it
            for ting in this:
                ting = ting.split(" ")
                if len(ting) == 1:
                    wordslist = Get_Def(ting)
                    make_collection(wordslist, name)
                name = next_name

morewords()

# if words != None:
    #     for word in words:
    #         # print(word)
    #         try:
    #             defs = Get_Def(word)
    #             make_collection(defs)
    #         except:
    #             continue

# morewords()





## when comes time to clean if word is repeated and has a row where its alone remove the one that is alone
## else leave it
#



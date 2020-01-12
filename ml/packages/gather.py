import pandas as pd
import os


def words():
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist")
    listdir = os.listdir(os.getcwd())
    words = None
    for file in listdir:
        with open(file, "r") as file:
            data = file.read()
            data.replace("\t","")
            data.replace("\n","")
            words = data.split(" ")

    if words != None:
        os.chdir("//home//noah//Desktop//Funstuff//ml//data//collection")
        name = os.listdir(os.getcwd())
        if name != []:
            name = list(map(int,name))
            replace(".csv", "")
            pd.DataFrame({"verb":words}).to_csv(str(max(name)+1)+".csv")
        else:
            pd.DataFrame({"verb":words}).to_csv("1.csv")


words()








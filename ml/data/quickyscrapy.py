from bs4 import BeautifulSoup
from requests import Session
import os

def get_text(url):
    ses = Session()
    text = ses.get(url).text

    return text


def make_soup(url):
    os.chdir("/home/noah/Desktop/Funstuff/ml/data/wordlist")
    soup = BeautifulSoup(get_text(url), 'html.parser')
    tb = soup.find_all("td",width=120)
    soupt = BeautifulSoup((str(tb)), 'html.parser')
    a = soupt.find_all("a")
    for n in a:
        with open("verblist3.txt", mode="a") as file:
            print(n.text)
            file.write(n.text+"\n")


# url = "https://www.talkenglish.com/vocabulary/top-1000-verbs.aspx"

make_soup(url)
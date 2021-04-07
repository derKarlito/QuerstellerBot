import requests
import urllib.request
from lxml import html
import urllib.request as ul
from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
import requests

from src.EventInfo import EventInfo


def GetCalender():
    url = "https://demo.terminkalender.top/pc.php"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")
    offset = 8
    ort = None
    Datum = None
    Uhrzeit = None
    Adresse = None
    Art = None
    Veranstalter = None
    for link in soup.find_all('td'):
        str = link.contents
        if len(str) != 0:
            if offset == 8:
                Datum = str[0]
            elif offset == 5:
                ort = str[0]
            elif offset == 4:
                Uhrzeit = str[0]
            elif offset == 3:
                Adresse = str[0]
            elif offset == 2:
                Art = str[0]
            elif offset == 1:
                Veranstalter = str[0]
        offset -= 1
        if offset == 0:
            offset = 8

    event = EventInfo(ort,Uhrzeit,Adresse,Art,Veranstalter,Datum)
    #TODO: get Name of City
    print(event)








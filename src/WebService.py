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

    eventInfos = []
    test = soup.find_all('td')
    index = 0
    for entry in test:
        if index <= 3:
            index += 1
            continue
        eventInfos.append(entry.text)

    Date = None
    Plz = None
    City = None
    Time = None
    Place = None
    How = None
    Organizer = None
    eventlist = []
    for i in range(0,len(eventInfos)-1,8):
        counter = 0
        for j in range(i,i+7):
            if counter == 0:
                Date = eventInfos[j]
                counter += 1
                continue
            if counter == 1:
                counter += 1
                continue
            if counter == 2:
                Plz = eventInfos[j]
                counter += 1
                continue
            if counter == 3:
                City = eventInfos[j].strip()
                counter += 1
                continue
            if counter == 4:
                Time = eventInfos[j]
                counter += 1
                continue
            if counter == 5:
                Place = eventInfos[j]
                counter += 1
                continue
            if counter == 6:
                How = eventInfos[j]
                counter += 1
                continue
            if counter == 7:
                Organizer = eventInfos[j]
                counter += 1
                continue

        eventlist.append(EventInfo(Plz,Time,Place,How,Organizer,Date,City))
    return eventlist






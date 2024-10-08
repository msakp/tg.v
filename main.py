#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as Bsoup
from settings import *



request = requests.get(URL + TEST_CHANNEL, headers=HEADERS)
print(request.headers)
soup = Bsoup(request.text, "lxml")
with open("log.html", 'w', encoding="utf-8") as ofile:
    ofile.write(soup.prettify())

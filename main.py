#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as Bsoup
from settings import *



responce = requests.get(URL + TEST_CHANNEL, headers={"User-Agent": USER_AGENT})

print(f"{responce.status_code} - {RESPONSE_CODE_TABLE[responce.status_code // 100]}")

soup = Bsoup(responce.text, "lxml")

# parse posts and channel info

# main content of tgstat.ru webpage
containerMain = soup.find("div").find("div").find("div").find_all("div", recursive=False)[1]

channelName = containerMain.find_all("div", recursive=False, limit=2)[1].find("div").find("div").find("div").find_all("div", recursive=False, limit=2)[1].find("h1").text.lstrip().rstrip()


# requested channel posts content
containerPosts = containerMain.find_all("div", recursive=False, limit=3)[2].find("div").find("div").find("div").find("form").find_all("div", recursive=False, limit=2)[1]

# parsing every post
posts = map(str, filter(lambda div: div.attrs.get("id") and div.attrs["id"].startswith("post-"), containerPosts.find_all("div"))) # converting Tag("div") objects to string


#posts = map(str, filter(lambda div: div.attrs.get("id") and div.attrs["id"].startswith("post-"),
#               soup.find_all("div")))    


# writing parsed posts output to log.html
with open("log.html", 'w', encoding="utf-8") as ofile:
    ofile.write('\n'.join(posts))



print(channelName)


import requests
import sys
from bs4 import BeautifulSoup as Bsoup
from tools import failed, makePost
from settings import URL, HEADERS

class ChannelClass:
    def __init__(self, name):
        try:
            responce = requests.get(URL + "/channel/" + name, headers=HEADERS)
            self.__responce_status_code = responce.status_code
            if failed(self.testChannelUrl()):
                raise BadChannelName


            soup = Bsoup(responce.text, "lxml")

            # parse posts and channel info

            # main content of tgstat.ru webpage
            containerMain = soup.find("div").find("div").find("div").find_all("div", recursive=False)[1]

            self.__channelName = containerMain.find_all("div", recursive=False, limit=2)[1].find("div").find("div").find("div").find_all("div", recursive=False, limit=2)[1].find("h1").text.lstrip().rstrip()


            # requested channel posts content
            containerPosts = containerMain.find_all("div", recursive=False, limit=3)[2].find("div").find("div").find("div").find("form").find_all("div", recursive=False, limit=2)[1]

            # parsing every post
            self.__posts = map(lambda div: makePost(div), filter(lambda div: div.attrs.get("id") and div.attrs["id"].startswith("post-"), containerPosts.find_all("div", recursive=False))) # converting Tag("div") objects to string
            
            self.__posts = map(str, self.__posts)
            

        except BadChannelName:
            print("invalid channel name.")
            sys.exit(0)

    def testChannelUrl(self):
        return self.__responce_status_code // 100 < 4

    
    def channelName(self):
        return self.__channelName
    def posts(self):
        return self.__posts

    def status(self):
        return self.__response_status_code



class BadChannelName(Exception):
    pass

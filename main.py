#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as Bsoup
from settings import *
from tools import *
from ChannelClass import ChannelClass

#channelName = input("enter channel name(must start with '@'):\n")


black_triangle = ChannelClass(channelName:="@black_triangle_tg")
with open("log.html", 'w', encoding="utf-8") as ofile:
    ofile.write('\n'.join(black_triangle.posts()))





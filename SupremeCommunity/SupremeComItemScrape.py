from SupremeCommunity.SupremeComSpider import get_SC_Page_Links, read_page
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from time import sleep

new = ["https://www.supremecommunity.com/season/fall-winter2017/droplists/"]

def get_SC_items(page):

    votes = page.findAll("div", {"class":"progress-bar"})
    name = page.findAll("h5", {"class": "name item-details"})
    price = page.findAll("span", {"class": "label-price"})

    return [votes,name,price]


def get_all_SC_items(url):

    pages = get_SC_Page_Links(url) # get list of links from pge
    weeks = []
    for page in range(len(pages)):
        parsed = get_SC_items(read_page((pages[page:]))) # just get one version to keep resource use low

        dbentry = [[], [], []] # 2d list to hold all features

        voteCount = str(parsed[0]).split("%;\">")  # gets votes per item
        itemNames = str(parsed[1]).split("<h5 class=\"name item-details\">")  # gets names of items
        prices = str(parsed[2]).split("<span class=\"label-price\">")  # gets prices of items

        for item in itemNames[1:]:   # enter each seperate name into this new array
            dbentry[0].append(item[:-7])

        for vote in range(2,len(voteCount),2):   # enter each seperate vote pair into this new array
            dbentry[1].append(str(voteCount[vote-1].split("</div")[0]) +
                              "," + str(voteCount[vote].split("</div")[0]))

        for itemPrice in prices[1:]: # enter each price into this new array
            dbentry[2].append(itemPrice.replace(" ", "").replace("\n", "")[:-8])

        weeks.append(dbentry)
        sleep(10)
    return weeks

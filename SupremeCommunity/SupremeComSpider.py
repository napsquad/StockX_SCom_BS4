from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from time import sleep

itemlist = []


def read_page(item):  #parse page

    for link in item:
        request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        parsed = soup(page, 'html.parser')
        return parsed


def search_page(page):
    testP = str(page.findAll("a", {"class":"block"})).split(",")
    for x in testP:
        itemlist.append((x[25:].split("\""))[0])


def get_SC_Page_Links(search): #get links from page
    new = read_page(search)
    search_page(new)

    for y in range(len(itemlist)):
        itemlist[y] = (search[0][:33] + itemlist[y])

    return itemlist
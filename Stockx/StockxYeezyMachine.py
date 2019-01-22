from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from time import sleep
from Stockx.StockxClothing import ClothItem
from Stockx.StockxShoe import ShoeItem
from pymongo import *

def read_page(item):

    for link in item:
        request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(request).read()
        parsed = soup(page, 'html.parser')

        return parsed


def extract_data(item):
    new =[]
    values = []
    new.append(item.findAll("div", {"class": "sale-value"}))
    details = item.findAll("div", {"class": "detail"})
    items = str(details).split('<div class="detail">')

    for y in new:
        newCost = str(y)[26:]
        arr = newCost.split("<")
        values.append(arr[0])

    for x in range(len(items)):
        if x == 0:
            print(" ")
        elif x ==1 or x==2:
            values.append(str(items[x])[75:].split(" ")[1])
        else:
            values.append(str(items[x])[75:].split(" ")[2])

    print("####################################################")
    print(values)
    test = ShoeItem(values[0], values[1], values[2], values[3], values[4])
    return test


def search_page(sPage):
    new = []

    new.append(sPage.findAll("div"))
    print(new)


itemlist = []
search = ["https://stockx.com/"]
base = "https://stockx.com/adidas-yeezy-boost-350-v2-"
models = ["static", "static-reflective", "sesame", "cream-white", "semi-frozen-yellow" ,
          "white-core-black-red", "butter", "beluga-2-0", "blue-tint", "core-black-red-2017",
          "core-black-white", "steeple-grey-beluga-solar-red", "core-black-copper",
          "core-black-red", "core-black-green", "oxford-tan",]


for page in models:
    new = read_page([base+page])
    Newitem = extract_data(new)
    itemlist.append(Newitem)
    Newitem.simpleCalc()
    sleep(3)

print(itemlist)

new = read_page(search)
print(new)
search_page(new)

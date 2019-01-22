import datetime


class ShoeItem:
    def __init__(self, setresale, setticker, setname, setretail, setreleaseday):
        self.ticker = setticker
        self.name = setname
        self.retail = setretail.split("$")[1]
        self.resale = setresale
        self.released =  setreleaseday
        self.date = datetime.datetime.now().date()  #date should be in ddmmyy format if possible

    def simpleCalc(self):

        timearr = self.released.split("-")
        diff = datetime.datetime.now() - datetime.datetime(int(timearr[0]),int(timearr[1]),int(timearr[2]))

        priceMultiplier = str( (((int(self.resale)) / int(self.retail)) -1) *100)
        daysPassed = (int(str(diff).split(" ")[0]))
        dChnge = (float((priceMultiplier)[:5])) / float(daysPassed)

        print(str(priceMultiplier)[:5]  + "%  more expensive than retail" +
              "\nDays since release: " + str(diff))

        print( str(dChnge)[:6] + " percent gained per day\n" + str((dChnge/100) * int(self.retail))[:6] + " dollars per day" )


class SC_item_info:

    def __init__(self, Setname, Setvotes, SetRetail):
        self.votes = Setvotes
        self.retail = SetRetail
        self.name = Setname

    def make_mongo_item(self):
        item = {
            "name": self.name,
            "retail": self.retail,
            "votes": self.votes
            }
        return item

    def print_name(self):
        print(self.name)
# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook


class Shirt:
    def __init__(self, sid = 100, sname = "Markss", stype = "Casual", price = 1000, size = "Medium"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def __del__(self):
        # print("Destructor is called.")
        pass

    def ShowBook(self):
        print(f"sid = {self.sid} sname = {self.sname} stype = {self.stype} price = {self.price} size = {self.size}")


s1 = Shirt(101, "US Polo", "Formal", 3600, "Large")
s2 = Shirt()

s1.ShowBook()
s2.ShowBook()
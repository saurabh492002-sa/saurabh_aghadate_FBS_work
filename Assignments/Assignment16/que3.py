# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.



class Shirt():

    z = 10

    # Constructor
    def __init__(self, sid = 101, sname = "Gucci", stype = "Casual", price = 1000, size = "M"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        pass

    # Showbook
    def ShowBook(self):
        print(f"sid = {self.sid} sname = {self.sname} stype = {self.stype} price = {self.price} size = {self.size} ")


    def Total_Price(self):
        if self.size == "S":
            self.price = self.price

        elif self.size == "M":
            self.price = self.price + (self.price * Shirt.z / 100)

        elif self.size == "L":
            self.price = self.price + (self.price * Shirt.z * 2 / 100)

        elif self.size == "M":
                    self.price = self.price + (self.price * Shirt.z * 3 / 100)

        



# Object
s1 = Shirt()
s2 = Shirt(102, "Uno", "Formal", 1000, "S")
s3 = Shirt(103, "Zara", "Casual", 1000, "L")

# Before Price Change
s1.ShowBook()
s2.ShowBook()
s3.ShowBook()


s1.Total_Price()
s2.Total_Price()
s3.Total_Price()

print("Total Price of Shirt is : ")

# After price change
s1.ShowBook()
s2.ShowBook()
s3.ShowBook()


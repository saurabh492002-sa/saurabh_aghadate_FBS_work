# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book:

    def __init__(self, bid = "0", bname = "abc", price = "0", author = "xyz"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        # print("Destructor is called.")
        pass

    def ShowBook(self):
        print(f"bid = {self.bid} bname = {self.bname} price = {self.price} author = {self.author} ")

b2 = Book(101, "Word Power", 250, "Goyal Saab")
b1 = Book()


b2.ShowBook()
b1.ShowBook()
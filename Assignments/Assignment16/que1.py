# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book():

    count = 0     # Static Variable

    def __init__(self, bid = 101, bname ="abc", price = 0, author ="xyz"):   # Method
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1




    def __del__(self):                                 # Destructor
        pass
        # print("Destructor is called.")

    def ShowBook(self):                                # Method
        print(f"bid = {self.bid} bname = {self.bname} price = {self.price} author = {self.author}")


b1 = Book()                                      # object
b2 = Book(102, "Python", 500, "James")           # object
b3 = Book(103, "Java", 800, "omlii")             # object

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

print("Total object created : ",Book.count)


    

    
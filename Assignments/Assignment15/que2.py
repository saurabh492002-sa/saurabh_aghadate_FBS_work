# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook


class Product():
    def __init__(self, pid = "0", pname = "aaa", price = "0", quantity= "0"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        # print("Destructor is call.")
        pass

    def ShowBook(self):
        print(f"pid = {self.pid} pname = {self.pname} price = {self.price} quantity = {self.quantity}")

p1 = Product(101, "Mobile", 45000, 10)
p2 = Product()


# p1.ShowBook()
p2.ShowBook()

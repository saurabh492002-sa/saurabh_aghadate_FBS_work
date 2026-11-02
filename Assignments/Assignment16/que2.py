# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.


class Product():

    Discount = 10
 

    def __init__(self, pid = 101, pname ="abc", price = 100, quantity ="1"):   # Method
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity


    def __del__(self):                                 # Destructor
        pass
        # print("Destructor is called.")

    def ShowProduct(self):                                # Method
        print(f"pid = {self.pid} pname = {self.pname} price = {self.price} quantity = {self.quantity}")


    def ApplyDiscount(self):
        self.price = self.price - (self.price * Product.Discount / 100)


b1 = Product()                                      # object
b2 = Product(102, "Mobile", 500, 3)           # object
b3 = Product(103, "Laptop", 800, 2)             # object

b1.ShowProduct()
b2.ShowProduct()
b3.ShowProduct()

print("After applying discount : ")

b1.ApplyDiscount()
b2.ApplyDiscount()
b3.ApplyDiscount()

b1.ShowProduct()
b2.ShowProduct()
b3.ShowProduct()



    

    
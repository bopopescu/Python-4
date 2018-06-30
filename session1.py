class product:

    def __init__(self,pid,name,price):
        self.pid=pid
        self.name=name
        self.price=price

    def showProduct(self):
        print(self.pid)


print(product.__dict__)

#IS-A relation


class book(product):

    def __init__(self,isbn,author,pid,name,price):
        super().__init__(pid,name,price)
        self.isbn=isbn
        self.author=author

    def showBook(self):
        print(self.isbn)


print(book.__dict__)

p1 = product(101, "ram", 20)
b1 = book(102,"ramesh")
print(b1.__dict__)
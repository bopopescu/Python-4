class point:
    def __init__(self,x,y,z):
        self.x=x
        self._y=y
        self.__z=z


p1 = point(10,20,30)
print("x",p1.x)
print("y",p1._y)
#print("z",p1.__z) error
print("z",p1._point__z)
print(p1.__dict__)

#name mangling - changing the name ofthe attribute
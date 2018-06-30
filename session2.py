class emp:

    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def showEmp(self):
        print(self.id)


eRef1=emp(101,"John",300000)

print(eRef1.__str__())
print(eRef1.__repr__())
#both return address

#del eRef1.name

print(eRef1.__dict__)
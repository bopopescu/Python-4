"""class Address:
    pass

class project:
    pass

class employee:
    def __init__(self,eid,name,salary,address,projects):

class softwareEngineer(employee):
    pass"""

class Teacher:

    def __init__(self, tid, name, contact, address, student):
        self.tid = tid
        self.name = name
        self.contact = contact
        self.address = address
        self.student = student

    def showTeacher(self):
        print()


class Subject(Teacher):

    def __init__(self, tid, name, contact, address, student, subjectName, subjectCode):
        super().__init__(tid, name, contact, address, student)
        self.subjectName= subjectName
        self.subjectCode = subjectCode

    def showSubject(self):
        print(self.tid,"  ",self.subjectName)

class Address:

     def __init__(self,adrsLine, city, zipCode):
        self.adrsLine  =adrsLine
        self.city = city
        self. zipCode = zipCode


class Student:

    def __init__(self,name,roll,year):
         self.name=name
         self.roll=roll
         self.year=year


a1 = Address("Country Lane","Ludhiana",141001)
StudentList = []
StudentList.append(Student("Ram",1410052,2015))
StudentList.append(Student("sham",1410352,2016))
t1= Teacher(141,"Tania","9999988888",a1,StudentList)
s1=Subject(141,"Tania","9999988888",a1,StudentList,"Geography",1526)
print(s1.__dict__)
s1.showSubject()

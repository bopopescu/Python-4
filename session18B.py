def dataGenerator():
    file = "studentsData.csv"
    for row in open(file,"r"):
        yield row

dg = dataGenerator()
print(type(dg))
print(next(dg))
print(next(dg))
print(next(dg))

for data in dg:
    print(data)
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plot
import pandas as pd
import sys
import matplotlib

"""print("Python version is ",sys.version)
print("Pandas version is ",pd.__version__)
print("Matpltlib version is ",matplotlib.__version__)

streams = ["cse","ece","me","pe"]
students=[200,170,230,90]

dataset = list(zip(streams,students))

#creates tuples for each set and is henceforth converted to list

print(dataset)

df = pd.DataFrame(data=dataset , columns=["streams","students"])
print(df)

df.to_csv("studentsData.csv",index=False,header=False)
print("DataFRAME WRITTEN")
#FILE CREATED LOCALLY IN THE PRACTICE MODULE"""



#df = pd.read_csv("studentsData.csv")
#print(df)
#df = pd.read_csv("studentsData.csv",header=None)
df = pd.read_csv("studentsData.csv",names = ["Streams","Students"])
print(df)

print(df.dtypes)

sdf = df.sort_values(["Streams"],ascending=False)
print(sdf.head(2))

nsdf = df.sort_values(["Students"],ascending=True)
print(nsdf.head(2))

print("Max number of students:",df["Students"].max())

df["Students"].plot()
maxStudents=df["Students"].max()
maxStream = df["Streams"][df["Students"] == df["Students"].max()].values


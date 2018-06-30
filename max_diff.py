a='1010101'
count=0
count2=0
for i in range(0,len(a)):
    if a[i]==1:
         count=i
         break


for i in range(len(a)-1,0,-1):
    if a[i]==1:
        count2=i
        break
    i+=1

print(count2-count+1)

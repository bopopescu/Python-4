def ing(a):
    if a.endswith("ing"):
        a = a+"ly"
    return a


print(ing("smiling"))


def sort(u_list):

    s_list = []
    for var in range(u_list:
        if var.startswith('x'):
            s_list.append(var)
            print(s_list)
            u_list.remove(var)

    s_list.sort()
    u_list.sort()
    s_list.extend(u_list)
    return s_list


print(sort(['apple', 'xavier', 'xan',  'mile']))


def rotate(input, d):

    rfirst = input[0: len(input) - d]
    rsecond = input[len(input) - d:]
    print("Right Rotation : ", (rsecond + rfirst))


rotate('helloWorld', 2)


m=2
n=8
b=0
s=[]
for x in range(0,n):
    s.append(0)
print(s)



while m>0:
    s[0] = 1
    b=(b+n)%m
    if b==0:
        s[b-1]=1
    else:
        break
print(s)
















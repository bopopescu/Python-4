def add(a,b):
    return a+b

fun=add

print(add(18,20))

print(type(fun))
print(type(add))

print(hex(id(add)))
print(hex(id(fun)))

#Lambdas|anonymous functions | single line functions
lm1=lambda x, y : x*y

print(type(lm1))
print(lm1(10,20))

#def square(num):
 #   return num*num

lm2 = lambda x, y : x*y
print(lm2(3,4))

def square(num1,num2):
    return num1*num2

#Maps
m1 = map(square,[1,2,3,4,5],[3,4,5,6,7])
print(m1)
print(type(m1))
print(list(m1))

#maps with lambdas and dictionary
emps = [{"eid":101,"name":"John"},{"eid":201,"name":"Jennie"}]
lm3=lambda dic : dic["name"]
result = map(lm3,emps)
print(list(result))


lm4= lambda dic: dic["name"] == "John"
result = map(lm4,emps)
print(list(result))

filterRes = filter(lm4,emps)
print(list(filterRes))

#multiple lists
lm5 = lambda p, q : p+q
l1=[10,20,30,40,50]
l2=[20,30,40,50,60]
result = map(lm5,l1,l2)
print(list(result))

#filters
l3=[1,2,3,4,5,6,7,8,9]
lm6=lambda n : n%2 == 0
result = map(lm6,l3)
print(list(result))

filterResult = filter(lm6,l3)
print(list(filterResult))

#list comprehensions
a = [1,2,3,4,5]
b = [x*x for x in[1,2,3,4,5]]
c = [x*x for x in[1,2,3,4,5] if x%2 == 0]
print(a)
print(b)
print(c)
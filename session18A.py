def show():
    return "A"

s=show

print(s())

#function can return only one value while yield results in more than one return statements

# Generator-> yields
def showAgain():
    yield "B"
    yield "c"

sa = showAgain()

print(sa)

print(type(s))
print(type(sa))

#generator in action
print(next(sa))
print(next(sa))


#decorator
#generator
#lambda
#regular expressions
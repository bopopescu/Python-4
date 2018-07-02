import re

quote = "Search the candle rather than cursing the darkness"

#result = re.match(r"the",quote)
result = re.match(r"Search",quote)
#checks the start element -> startswith and endswith
print(result)
print(type(result))
print(result.start())
print(result.end())
print("********************")

result = re.search(r"the",quote)
#checks the containment of the variable
print(result.group(0))
print("********************")
result = re.findall(r"the",quote)
print(result)
print("********************")
result = re.split(r"the",quote)
print(result)
print(type(result))
print("********************")
result = re.sub(r"the","a",quote)
print(result)
print("********************")

pattern = re.compile("the")
result = pattern.findall(quote)
print(type(pattern))
print(result)

print("********************")


quote = "work hard and get luckier"
result = re.findall(r".",quote)
print(result)

print("********************")

result = re.findall(r"\w",quote)
print(result)

print("********************")

result = re.findall(r"\w*",quote)
print(result)

print("********************")

result = re.findall(r"\w+",quote)
print(result)

email = "abc@gmail.com"
phone = "+91 98159 03689"

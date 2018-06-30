import requests
from bs4 import BeautifulSoup

response = requests.get("http://zeenews.india.com/")
soup = BeautifulSoup(response.text,"html.parser")

print("Fetching data for: "+soup.title.text)

dTags = soup.find_all('div', class_="mini-con")
print(dTags[0])
print("*****************")
print(dTags[0].text)

for tags in dTags:
    print(tags.text)

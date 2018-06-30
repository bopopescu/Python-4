import requests
from bs4 import BeautifulSoup

response = requests.get("https://twitter.com/dna")

soup = BeautifulSoup(response.text, "html.parser")
"""print(soup)
print(type(soup))
print(soup.prettify())
print("Fetching data for: "+soup.title.text)"""

"""children = soup.children

for child in children:
    print(child)
    print("******************")"""

"""ptags = soup.find_all('p')#similar for all tags
for tags in ptags:
    print(tags)"""

dTags = soup.find_all('div', class_="js-tweet-text-container")
print(dTags[0])
print("*****************")
print(dTags[0].text)
for tags in dTags:
    print(tags.text)




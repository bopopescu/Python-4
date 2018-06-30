import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup = BeautifulSoup(response.text,"html.parser")

print("Fetching data for: "+soup.title.text)

dTags = soup.find_all('td', class_="titleColumn")
print(dTags[0])
print("*****************")
print(dTags[0].text)

movies = []

for tags in dTags:
    print(tags.text)
    movies.append(tags.text.strip())
    print("********************************")

print("********************************")
for movie in movies:
    print(movie)

dTags = soup.find_all('td', class_="ratingColumn")
print(dTags[0].find("strong").text)


for tags in dTags:
    if tags.find("strong") is not None:
        print(tags.find("strong").text)

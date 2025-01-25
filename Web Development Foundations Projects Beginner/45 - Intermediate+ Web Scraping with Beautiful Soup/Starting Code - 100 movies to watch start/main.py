import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
archive_website = response.text

soup = BeautifulSoup(archive_website, 'html.parser')

movie_titles = soup.select(selector=".article-title-description__text h3")
movie_titles.reverse()

with open('movies.txt', 'w') as file:
    for movie in movie_titles:
        file.write(f"{movie.getText()}\n")

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

headings = soup.select(selector=".titleline a")
heading_upvotes = soup.select(selector=".score")

article_titles = [heading.getText() for heading in headings]
article_links = [heading.get("href") for heading in headings]
article_scores = [int(upvote.getText().split()[0]) for upvote in heading_upvotes]

# print(article_titles)
# print(article_links)
# print(article_scores)

maximal_score = max(article_scores)
index_max = article_scores.index(maximal_score)
print(f"Title : {article_titles[index_max]} \nLink: {article_links[index_max]}")
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tag = soup.find_all(name="a")
#
# for tag in all_anchor_tag:
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.get(""))
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# headings = soup.select(selector=".heading")
# for heading in headings:
#     print(heading.get("class"))

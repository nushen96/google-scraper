import urllib
import requests
from bs4 import BeautifulSoup
import json

keywords = ["apple","banana","pear"]
results = []
def crawl(keyword):
  url = f"https://google.com/search?q={keyword}"

  platform = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

  headers = {"user-agent": platform}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
  for elem in soup.find_all('div', class_="r"):
    links = elem.find_all('a')
    if links:
      url = links[0]['href']
      title = elem.find('h3').text
      result = {
        "title": title,
        "url": url,
        "keyword": keyword
      }
      results.append(result)
for keyword in keywords:
  crawl(keyword)
f = open("results.json", "a")
f.write(json.dumps(results))
f.close()

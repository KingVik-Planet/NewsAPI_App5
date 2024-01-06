# Importing modules
import requests

#API Key and the url
api_key = "cc2ef8f1b8854e388d11e45720601b8c"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-06&sortBy=publishedAt&apiKey=cc2ef8f1b8854e388d11e45720601b8c"
requests = requests.get(url)
content = requests.json()

# print(content["articles"])
#Printing the Content
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
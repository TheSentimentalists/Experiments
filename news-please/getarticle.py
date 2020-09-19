from newsplease import NewsPlease
import sys

try:
    url = sys.argv[1]
except IndexError:
    raise SystemExit("Specify a URL: python3 getarticle.py https://www.bbc.co.uk/news/uk-54214752")

article = NewsPlease.from_url(url)
print("Title: {}".format(article.title))
print("Summary: {}".format(article.description))
print("Body: {}".format(article.maintext))
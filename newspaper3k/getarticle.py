from newspaper import Article
import sys

try:
    url = sys.argv[1]
except IndexError:
    raise SystemExit("Specify a URL: python3 getarticle.py https://www.bbc.co.uk/news/uk-54214752")

article = Article(url)
article.download()
article.parse()
print("Title: {}".format(article.title))
print("Body: {}".format(article.text))
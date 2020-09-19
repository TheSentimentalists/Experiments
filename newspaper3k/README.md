# newspaper3k
An experiment to test newspaper3k's article-fetching capability

# Install
This experiment is setup with pipenv. To install it, run:

```pipenv install```

This will create a virtual environment and obtain the necessary dependencies (newspaper3k) with pip.

# Run
The following command will run the script, fetch your URL and parse it:

```pipenv run python3 getarticle.py <your article url>```

# Results (so far)
This seems like a potential candidate for fetching articles, however, does have some limitations:
- Full article text is not always retrieved (assume because of ads?)
- Feeding newspaper3k non-article pages has some unexpected results
- GDPR warnings/robot checks cause some problems (huffpost/amazon article)
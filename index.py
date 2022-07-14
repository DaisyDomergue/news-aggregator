from typing import Union

from fastapi import FastAPI
import pandas as pd
import requests
import requests.auth
import json

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

SEARCH_URL_NEWSAPI = "https://newsapi.org/v2/everything?"
LATEST_URL_NEWSAPI = "https://newsapi.org/v2/top-headlines?"

SEARCH_URL_REDDIT = "https://www.reddit.com/r/news/search.json?"
LATEST_URL_REDDIT = "https://www.reddit.com/r/news/hot.json?"

app = FastAPI()


@app.get("/")
async def get_latest_news(): 
    return search_reddit_news() + search_newsapi()


@app.get("/search/{query}")
async def get_news_by_topic(query):
    
    return search_reddit_news(query) + search_newsapi(query)

def proccess_newsapi_response(articles):
    df=pd.DataFrame(articles)
    df=df.rename(index=str, columns={"source": "from", "title": "headline","url":"link"})
    df=df.drop(['from', 'author','description','urlToImage','publishedAt','content'], axis=1)
    df['source'] = "newsapi"
    return df.to_dict('records')

def search_newsapi(query=""):
    if query != "":
        url_root = SEARCH_URL_NEWSAPI
        payload="q="+query
    else:
        url_root = LATEST_URL_NEWSAPI
        payload="country=us"
    headers = {}
    headers['x-api-key'] = "6aebb03a996f4961ab65c5d62508f867"
    url = url_root + payload
    response = requests.request("GET", url, headers=headers)
    return proccess_newsapi_response(response.json()['articles'])

def search_reddit_news(query=""):
    if query != "":
        reddit_url = SEARCH_URL_REDDIT
        payload="q="+query
    else:
        reddit_url = LATEST_URL_REDDIT
        payload=""
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_7 rv:5.0; en-US) AppleWebKit/533.31.5 (KHTML, like Gecko) Version/4.0 Safari/533.31.5',
    }
    
    CLIENT_ID = "PIZqgdF-mnIa4NnhA7HM0Q"
    CLIENT_SECRET = "1YuWS9pqNcJk_wVrvRwOkF7UXfHqrg"
    url = reddit_url + payload
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
    response = requests.request("GET", url, auth=client_auth, headers=headers)
    return proccess_reddit_response(response.json()['data']['children'])

def proccess_reddit_response(articles):
    a = [{**x, **x.pop('data')} for x in articles]
    df = pd.DataFrame(a)
    df.drop(df.columns.difference(['title','url']), 1, inplace=True)
    df=df.rename(index=str, columns={"source": "from", "title": "headline","url":"link"})
    df['source'] = "reddit"
    return df.to_dict('records')
    
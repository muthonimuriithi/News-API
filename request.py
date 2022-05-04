from concurrent.futures import process
import json
from time import time
from app import loise
import urllib.request ,json
from .models import news

new= news.News()

api_key = loise.config['NEWS_API_KEY'] #f51300cb046c40219d0804da1c5cd5eb

base_url = loise.config['NEWS_API_BASE_URL'] 

def get_news(popularity):
    get_news_url = base_url.format(popularity, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read() 
        get_news_response= json.loads(get_news_data)

        news_results=None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results= process_news;{news_results_list}

        return news_results

def process_news(news_list):
    news_results= []
    for news_item in news_list:
        image = news_item.get('image')
        description= news_item.get('description')
        time = news_item.get('time')

        news_results.append(description)
        return news_results


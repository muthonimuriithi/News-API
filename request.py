from concurrent.futures import process
import json
from app import loise
import urllib.request ,json
from .models import news

new= news.News()

api_key = loise.config['NEWS_API_KEY'] #f51300cb046c40219d0804da1c5cd5eb

base_url = loise.config['NEWS_API_BASE_URL'] 

def get_news(category):
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read() 
        get_news_response= json.loads(get_news_data)

        news_results=None

        if get_news_response['results']
        news_results= process_results{news_results_list}

        return news_results

    def process_results(news_list):
        news_results= []
        if item in news_list:
            

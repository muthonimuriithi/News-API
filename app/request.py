import urllib.request
import json
from webbrowser import get
from .models.news import Article, Source


api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config.get('NEWS_API_KEY')
    base_url = app.config.get('NEWS_API_BASE_URL')


def get_news(category=None, source=None):
    get_news_url = None
    if category != None:
        get_news_url = base_url.format(
            f'top-headlines?category={category}&language=en', api_key)
    elif source != None:
        get_news_url = base_url.format(
            f'top-headlines?sources={source}&language=en', api_key)
    else:
        get_news_url = base_url.format(
            'top-headlines?language=en', api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)
    return news_results


def process_news(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        author = news_item.get('author')
        date = news_item.get('publishedAt')
        description = news_item.get('description')
        url = news_item.get('url')
        url_to_image = news_item.get('urlToImage')
        if url_to_image:
            news = Article(title, author, date, description, url, url_to_image)
            news_results.append(news)
    return news_results


def get_sources():
    get_sources_url = base_url.format(
        'sources?language=en', api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_response['sources']:
            sources_results_list = sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results


def process_sources(sources_list):
    sources = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        source_object = Source(id, name)
        sources.append(source_object)
    return sources

from flask import render_template
from .request import get_news, get_sources
from app.main import main


@main.route('/')  # localhost5000/
def index():
    articles = get_news('general')  # top-headlines articles
    sources = get_sources()  # all available news sources
    return render_template('index.html', sources=sources, articles=articles)


@main.route('/category/<string:category>')
def category(category):
    sources = get_sources()  # all available news sources
    articles = get_news(category, None)
    return render_template('index.html', sources=sources, articles=articles)


@main.route('/source/<string:source>')
def source(source):
    sources = get_sources()  # all available news sources
    articles = get_news(None, source)
    return render_template('index.html', sources=sources, articles=articles)

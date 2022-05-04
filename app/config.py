import os
from pickle import FALSE


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = False


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'production': ProdConfig,
    'development': DevConfig
}

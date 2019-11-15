import os
class Config:
    '''
    general configuartion of parent class
    '''
    category = 'popular'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key=184944fea9982650e27bcfbf22942d8f'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass

class ProdConfig (Config):
    '''
    Production configuration child class
    
    Args:
    Config:thne parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Production configuration child class

    Args:
        Config:the parent configuration class with general configuration settings
    '''
    pass

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


class Config:
    '''
    general configuartion of parent class
    '''
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
    

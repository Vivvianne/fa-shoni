class Config:
    '''
    The main configuration settings
    '''
    pass
class ProConfig(Config):
    '''
    Production child class for the configuration class
    Args:
    Config:The main configuration setting class
    '''
    pass
class DevConfig(Config):
    '''
    Development child class for the configuration setting
    Args:
    Config:THe configuration main class
    '''
    DEBUG = True 
config_options = {
    'development':DevConfig,
    'production':ProConfig
}

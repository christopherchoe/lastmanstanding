class BaseConfig(object):
    ''' Base Config Class '''
    DEBUG = True
    TESTING = False

class ProductionConfig(BaseConfig):
    ''' Production Config '''
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    ''' Development specific Config '''
    DEBUG = True
    TESTING = True


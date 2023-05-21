##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = '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'


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

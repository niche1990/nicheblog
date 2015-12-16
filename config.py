from os import path

class Config:
    DEBUG = True
    BLOGER_NAME = 'niche'
    BLOGER_PASSWORD = '05110511'
    CRT_PATH = path.join(path.dirname(__file__), 'blog')

if __name__ == '__main__':
    for key,val in Config.__dict__.iteritems():
        if not key.startswith('__'):
            print key,'=>',val

'''
random photo helper module
(c) 2018 - laymonage
'''

import requests


def randompic():
    '''
    Return a random pic.
    '''
    url = 'http://picsum.photos/720/480/?random'
    req = requests.get(url)
    url = req.url.replace('http://', 'https://')
    return url

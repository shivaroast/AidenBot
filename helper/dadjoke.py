'''
dadjoke helper module
(c) 2018 - laymonage
'''

import requests


def cat():
    '''
    Return a dad joke.
    '''
    url = 'http://icanhazdadjoke.com/'
    req = requests.get(url)
    url = req.url.replace('http://', 'https://')
    return url

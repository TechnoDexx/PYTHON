"""
Created on 30.01.2015

@author: Владелец
"""
import urllib.request
import urllib.response


def gethtml(url):
    response = urllib.request.urlopen(url)
    return response.read()


def html():
    print('html')

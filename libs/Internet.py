'''
Created on 30.01.2015

@author: Владелец
'''
import urllib.request

def GetHTML(url):
    response=urllib.request.urlopen(url)
    return response.read()
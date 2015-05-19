'''
Created on 30.01.2015

@author: Владелец
'''
import urllib.request
import urllib.response

def GetHTML(url):
    response=urllib.request.urlopen(url)
    return response.read()
def HTML():
    print('HTML')
'''
created on 01.02.2015

@author: владелец
'''
import os

from libs import hello
from test import test
from libs import internet

hello.sayhello()
test.test()
print(os.environ['home'])
print(internet.gethtml('http://mail.ru'))
internet.html()

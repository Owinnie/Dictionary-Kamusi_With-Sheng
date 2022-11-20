#!/usr/bin/python3
""" Populate the tables """

from main import *


conn = engine.connect()
conn.execute(words.insert(), [
    {'word': 'a', 'pronun': '/ae/',
     'def': 'The first letter of the alphabet; used in singular form',
     'ssent': 'This is a book', 'Swa': 'a', 'Sheng': 'a'},
    {'word': 'ability', 'pronun': '/əbiliti/',
     'def': 'Having the power, strength, and or skill to do something',
     'ssent': 'She has the ability to save the company',
     'Swa': 'uwezo', 'Sheng': ''},
    {'word': 'accept', 'pronun': '/əksept/',
     'def': 'Agree; consent',
     'ssent': 'He finally agreed to take out the trash',
     'Swa': 'kubali', 'Sheng': 'sambatawa'},
    {'word': 'add', 'pronun': '/ad/',
     'def': 'Join or put together; [in Math: + /plus sign/]',
     'ssent': 'Kindly add me to the Achiever\'s whatsapp group',
     'Swa': 'ongeza', 'Sheng': 'adisia'},
    {'word': 'afraid', 'pronun': '/əfreid/',
     'def': 'Scared; fear; anxious',
     'ssent': 'I am afraid to check the end term results just posted',
     'Swa': 'ogopa', 'Sheng': 'haha/gwaya/kunja mkia/kuingiza waba'},
])

#!/usr/bin/python3
""" Populate the tables """

from main import *


conn = engine.connect()
conn.execute(words4.insert(), [
    {'word': 'o', 'pronun': '/o\'/',
     'def': 'Fourth vowel letter / sound',
     'ssent': 'Ooo nooo'},
    {'word': 'obey', 'pronun': '/əo\'bei/',
     'def': 'Follow or conform to rules set',
     'ssent': 'Trust and obey, for there\'s no...'},
    {'word': 'office', 'pronun': '/ofis/',
     'def': 'Building or room-space used for proffesional purposes',
     'ssent': 'She works a 9-5 office job'},
    {'word': 'only', 'pronun': '/onli/',
     'def': 'One of its kind',
     'ssent': 'He is the only son of is mother.'},
    {'word': 'original', 'pronun': '/oridjinal/',
     'def': 'Unique',
     'ssent': 'An original LV bag goes for 50 dollars'},
])

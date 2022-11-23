#!/usr/bin/python3
""" Populate the tables """

from main import *


conn = engine.connect()
conn.execute(words5.insert(), [
    {'word': 'u', 'pronun': '/a/',
     'def': 'Last vowel letter / sound',
     'ssent': ' ',
     'Swa': 'u', 'Sheng': ''},
    {'word': 'ugly', 'pronun': '/əgle/',
     'def': 'Not pretty or not beautiful',
     'ssent': 'That is an ugly skirt!',
     'Swa': 'mbaya', 'Sheng': 'kiatu[kee-a-too]/shipwepwe'},
    {'word': 'uncle', 'pronun': '/əNGkkl/',
     'def': 'The brother to your mother or father',
     'ssent': 'I have an amazing uncle',
     'Swa': 'mjomba', 'Sheng': 'ankules'},
    {'word': 'university', 'pronun': '/juniversiti/',
     'def': 'An institution of higher learning',
     'ssent': 'A [proud] comrade from a public Kenyan univesity',
     'Swa': 'Chuo Kikuu', 'Sheng': 'yuni/campo'},
    {'word': 'understand', 'pronun': '/anderstand/',
     'def': 'get the intended meaning being passed across',
     'ssent': 'A good understanding of languages is desirable',
     'Swa': 'elewa', 'Sheng': 'gitch'},
])

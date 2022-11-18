#!/usr/bin/python3
""" Populate the tables """

from main import *


conn = engine.connect()
conn.execute(words3.insert(), [
    {'word': 'i', 'pronun': '/i/',
     'def': 'First person pronoun',
     'ssent': 'I am an online based dictionary'},
    {'word': 'ignore', 'pronun': '/igno/',
     'def': 'Avoid; not caring about something',
     'ssent': 'She ignored my calls the whole day'},
    {'word': 'image', 'pronun': '/imadj/',
     'def': 'Representation of sth via art; impression',
     'ssent': 'The artist drew and image of me on paper'},
    {'word': 'income', 'pronun': '/inkum/',
     'def': 'Money received on reqular intervals; salary',
     'ssent': 'His income was enough to start a family'},
    {'word': 'individual', 'pronun': '/individjual/',
     'def': 'A person',
     'ssent': 'Each individual is responsible for his or her actions'},
])

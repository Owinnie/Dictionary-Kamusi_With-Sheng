#!/usr/bin/python3
""" Populate the tables """

from main import *


conn = engine.connect()
conn.execute(words2.insert(), [
    {'word': 'e', 'pronun': '/e/',
     'def': 'Second vowel letter; 5th letter of Roman alphabet',
     'ssent': 'Grade E equals fail in some institutions',
     'Swa': 'e', 'Sheng': 'e'},
    {'word': 'eat', 'pronun': '/it/',
     'def': 'Consume or ingest something using your mouth',
     'ssent': 'She eats bananas in the morning',
     'Swa': 'kula', 'Sheng': 'bonda/dimbua/bonya/dema/manga'},
    {'word': 'egg', 'pronun': '/eg/',
     'def': 'germ cell, ovum, zygote; [consumable]produced by birds',
     'ssent': 'Make me an egg sandwich',
     'Swa': 'yai', 'Sheng': 'yayo/boiro'},
    {'word': 'empty', 'pronun': '/emti/',
     'def': 'Not occupied; having nothing',
     'ssent': 'An empty street an empty house ...',
     'Swa': 'tupu', 'Sheng': 'kirai/bila/bilaz'},
    {'word': 'end', 'pronun': '/end/',
     'def': 'Finish; maximum; final',
     'ssent': 'All good things come to an end',
     'Swa': 'isha/mwisho', 'Sheng': 'fini/shai/mapronye'},
])

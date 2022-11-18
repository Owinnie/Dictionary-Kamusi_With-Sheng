#!/usr/bin/python3
""" a-Words Table """

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


engine = create_engine("mysql+pymysql://owinnie:3aJesus$@localhost/onDict",
                       echo=True)
meta = MetaData()

words = Table(
    'aWords', meta,
    Column('word', String(355), primary_key=True),
    Column('pronun', String(255)),
    Column('def', String(555)),
    Column('ssent', String(455)),
)

words2 = Table(
    'eWords', meta,
    Column('word', String(355), primary_key=True),
    Column('pronun', String(255)),
    Column('def', String(555)),
    Column('ssent', String(455)),
)

words2 = Table(
    'iWords', meta,
    Column('word', String(355), primary_key=True),
    Column('pronun', String(255)),
    Column('def', String(555)),
    Column('ssent', String(455)),
)

words2 = Table(
    'oWords', meta,
    Column('word', String(355), primary_key=True),
    Column('pronun', String(255)),
    Column('def', String(555)),
    Column('ssent', String(455)),
)

words2 = Table(
    'uWords', meta,
    Column('word', String(355), primary_key=True),
    Column('pronun', String(255)),
    Column('def', String(555)),
    Column('ssent', String(455)),
)
meta.create_all(engine)

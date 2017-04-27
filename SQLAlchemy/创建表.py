#!/usr/bin/env python
# coding:utf-8

"""
    先pip安装sqlalchemy
"""

import sqlalchemy

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=True)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'

    extend_existing = True

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    age = Column(Integer)

    def __str__(self):
        return 'User(id={}, name={}, age={})'.format(self.id, self.name, self.age)


Base.metadata.create_all(engine)

Base.metadata.drop_all(engine)


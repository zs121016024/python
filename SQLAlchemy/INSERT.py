#!/usr/bin/env python
# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/demo', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()           #生成Model类的基类


from sqlalchemy import Column, Integer, String

class User(Base):       #继承Base基类
    __tablename__ = 'user'      #表名

    extend_existing = True

    id = Column(Integer, autoincrement=True, primary_key=True)      #字段id
    name = Column(String(64), unique=True, nullable=False)          #字段name
    age = Column(Integer)                                           #字段age

    def __str__(self):      #不是必须的，目的是为了调试，生产环境不需要
        return 'User(id={}, name={}, age={})'.format(self.id, self.name, self.age)

Session = sessionmaker(bind=engine)

session = Session()

user = User()
user.name = 'zhangsong'
user.age = 20

session.add(user)
session.commit()
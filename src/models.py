import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(15), primary_key=True) 
    email = Column(String(25), nullable=False) 
    password = Column(String(30), nullable=False) 
    posts = relationship("Post", back_populates="autor") 
    likes = relationship("Likes", back_populates="user")  
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(String(15), primary_key=True) 
    user_id = Column(String(15), ForeignKey('user.id')) 
    content = Column(String(250), nullable=True) 
    autor = relationship("User ", back_populates="posts") 
    likes = relationship("Likes", back_populates="post") 

    def to_dict(self):
        return {}

class Likes(Base): 
    __tablename__ = 'likes' 
    id = Column(Integer, primary_key=True) 
    user_id = Column(String(15), ForeignKey('user.id'))  
    post_id = Column(String(15), ForeignKey('post.id'))  
    user = relationship("User ", back_populates="likes") 
    post = relationship("Post", back_populates="likes") 

    def to_dict(self):
        return {}

class Follower(Base): 
    __tablename__ = 'follower'  
    id = Column(Integer, primary_key=True) 
    follower_id = Column(String(15), ForeignKey('user.id'))  
    user_id = Column(String(15), ForeignKey('user.id'))  

    def to_dict(self):
        return {}

class Following(Base): 
    __tablename__ = 'following' 
    id = Column(Integer, primary_key=True) 
    follower_id = Column(String(15), ForeignKey('user.id')) 
    user_id = Column(String(15), ForeignKey('user.id'))  

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorites = relationship('Favorite', back_populates='user')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))
    height = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))

    favorites = relationship('Favorite', back_populates='character')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(String(50))
    diameter = Column(String(50))

    favorites = relationship('Favorite', back_populates='planet')


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')


try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! El archivo diagram.png ha sido generado.")
except Exception as e:
    print("Hubo un error al generar el diagrama")
    print(e)

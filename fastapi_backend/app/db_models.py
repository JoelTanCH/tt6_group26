from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    refresh_token = Column(String)

    wallets = relationship("Wallet", back_populates="user", cascade="all, delete, delete-orphan")

    # projects = relationship("Project", back_populates="user",
    #                         cascade="all, delete, delete-orphan")

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="wallets")

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    amount = Column(Float)
    wallet_id = Column(Integer, ForeignKey("wallets.id"))

    wallet = relationship("Wallet", back_populates="currencies")


class ExchangeRate(Base):
    __tablename__ = "exchangerates"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String)
    exchange_currency = Column(String)
    rate = Column(Float)
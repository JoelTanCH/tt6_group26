from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    refresh_token = Column(String) # for jwt

    wallets = relationship("Wallet", back_populates="user", cascade="all, delete, delete-orphan")

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="wallets")
    currencies = relationship("Currency", back_populates="wallet", cascade="all, delete, delete-orphan")
    transactions = relationship("Transaction", back_populates="wallet", cascade="all, delete, delete-orphan")

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String)
    amount = Column(Float)
    wallet_id = Column(Integer, ForeignKey("wallets.id"))

    wallet = relationship("Wallet", back_populates="currencies")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"))

    debit_id = Column(Integer, ForeignKey("currencies.id"))
    debit_currency = Column(String)
    debit_amount = Column(Float)

    credit_id = Column(Integer, ForeignKey("currencies.id"))
    credit_currency = Column(String)
    credit_amount = Column(Float)

    created_at = Column(DateTime)
    created_by = Column(String)
    updated_at = Column(DateTime)
    updated_by = Column(String)

    wallet = relationship("Wallet", back_populates="transactions")




class ExchangeRate(Base):
    __tablename__ = "exchange_rate"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String)
    exchange_currency = Column(String)
    rate = Column(Float)



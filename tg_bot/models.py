import datetime
from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, ForeignKey, \
    create_engine, BigInteger

from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()
engine = create_engine(os.environ['DBURL'])


class Product(Base):
    __tablename__ = "web_product"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    price_start = Column(Integer)
    price_end = Column(Integer)
    time = Column(Integer)
    img = Column(String(150))
    image = Column(String(150))

class Order(Base):
    __tablename__ = "web_order"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    email = Column(String(120), index=True)
    phone = Column(String(15))
    content = Column(String(1000), nullable=False)
    created_on = Column(DateTime(), default=datetime.datetime.now)
    is_confirm = Column(Boolean(), default=False)
    is_pay = Column(Boolean(), default=False)

class ProductInOrder(Base):
    __tablename__ = "web_product_in_order"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer(), ForeignKey('order.id'))
    product_id = Column(Integer(), ForeignKey('product.id'))

from app import db
import datetime
from sqlalchemy import Table, Index, Integer, String, Column, Text, \
    DateTime, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, ForeignKey, \
    create_engine, BigInteger


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    price = Column(Integer)
    time = Column(Integer)
    image = Column(String(150))

class Order(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    email = Column(String(120), index=True)
    phone = Column(String(15))
    content = Column(String(1000), nullable=False)
    created_on = Column(DateTime(), default=datetime.datetime.now)

class ProductInOrder(db.Model):
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer(), ForeignKey('order.id'))
    product_id = Column(Integer(), ForeignKey('product.id'))

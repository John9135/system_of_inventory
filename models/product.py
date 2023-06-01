from sqlalchemy import Column, Integer, String, Float, Date
from config.database import Base


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    brand = Column(String)
    Description = Column(String)
    price = Column(Float)
    entry_date = Column(Date)
    availability = Column(String)
    available_quantity = Column(Integer)
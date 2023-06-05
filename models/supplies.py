from sqlalchemy import Column, Integer, Float, ForeignKey
from config.database import Base

class Supplies(Base):

    __tablename__ = "supplies"

    id = Column(Integer, primary_key = True)
    sup_id = Column(Integer,ForeignKey("supplier.id"))
    pro_id = Column(Integer, ForeignKey("product.id"))
    purchase_price = Column(Float)
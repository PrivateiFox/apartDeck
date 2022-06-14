from sqlalchemy import Column, Integer, String, Index, Boolean

from database import Base


class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, index=True, unique=True)
    city = Column(String, index=True)
    street = Column(String)
    apartment_price = Column(Integer)
    hoa_price = Column(Integer)
    rates_price = Column(Integer)
    notes = Column(String)
    phone_number = Column(Integer, index=True)
    is_valid = Column(Boolean, index=True)

    # UniqueConstraint('link', 'phone_number', name='link_phone_relation')
    Index('link_to_phone', 'link', 'phone_number', unique=True)

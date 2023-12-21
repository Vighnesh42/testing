from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    origin = Column(String)
    destination = Column(String)
    depart_time = Column(DateTime)
    depart_weekday = Column(Integer)
    duration = Column(String)
    arrival_time = Column(DateTime)
    arrival_weekday = Column(Integer)
    flight_no = Column(String)
    airline_code = Column(String)
    airline = Column(String)
    economy_fare = Column(Float)
    business_fare = Column(Float)
    first_fare = Column(Float)
    check_in_baggage = Column(String)
    cabin_baggage = Column(String)
    meal = Column(String)
    cancellation = Column(String)
    origin_name = Column(String)
    destination_name = Column(String)

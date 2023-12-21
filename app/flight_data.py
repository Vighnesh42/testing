import csv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

# Define the SQLite database file path
DATABASE_URL = "sqlite:///flights.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Declarative base
Base = declarative_base()

# Define the ORM class for the table
class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    origin = Column(String)
    destination = Column(String)
    depart_time = Column(DateTime)
    depart_weekday = Column(Integer)
    duration = Column(String)  # Store duration as string
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

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Path to your CSV file
csv_file = "C:/Users/Vaishnvi V Ballur/Documents/Python/app/flights_final.csv"

# Read data from CSV and insert into the database
with open(csv_file, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Parse duration string to timedelta object
        duration_parts = row["duration"].split(":")
        duration = timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]), seconds=int(duration_parts[2]))

        # Validate and handle empty or non-numeric values for fares
        try:
            economy_fare = float(row["economy_fare"]) if row["economy_fare"] else None
            business_fare = float(row["business_fare"]) if row["business_fare"] else None
            first_fare = float(row["first_fare"]) if row["first_fare"] else None
        except ValueError:
            economy_fare = None
            business_fare = None
            first_fare = None

        # Assign non-numeric columns directly as strings
        check_in_baggage = row["check_in_baggage"]
        cabin_baggage = row["cabin_baggage"]
        origin_name = row["origin_name"]
        destination_name = row["destination_name"]

        flight = Flight(
            index=int(row["index"]),
            origin=row["origin"],
            destination=row["destination"],
            depart_time=datetime.strptime(row["depart_time"], "%H:%M:%S"),
            depart_weekday=int(row["depart_weekday"]),
            duration=str(duration),  # Store duration as string
            arrival_time=datetime.strptime(row["arrival_time"], "%H:%M:%S"),
            arrival_weekday=int(row["arrival_weekday"]),
            flight_no=row["flight_no"],
            airline_code=row["airline_code"],
            airline=row["airline"],
            cancellation=row["cancellation"],
            meal=row["meal"],
            economy_fare=economy_fare,
            business_fare=business_fare,
            first_fare=first_fare,
            check_in_baggage=check_in_baggage,
            cabin_baggage=cabin_baggage,
            origin_name=origin_name,
            destination_name=destination_name
        )
        session.add(flight)

# Commit changes and close the session
session.commit()
session.close()

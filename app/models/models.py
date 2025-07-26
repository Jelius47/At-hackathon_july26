from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)

    plots = relationship("Plot", back_populates="owner")

class Drone(Base):
    __tablename__ = "drones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_available = Column(Boolean, default=True)

    plots = relationship("Plot", back_populates="drone")

class Plot(Base):
    __tablename__ = "plots"
    id = Column(Integer, primary_key=True, index=True)
    size_in_acres = Column(Float)
    number_of_drones = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    drone_id = Column(Integer, ForeignKey("drones.id"))

    owner = relationship("User", back_populates="plots")
    drone = relationship("Drone", back_populates="plots")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True)
    amount = Column(Float)
    buyer_name = Column(String)
    buyer_email = Column(String)
    buyer_phone = Column(String)
    extra_data = Column(JSON)
    status = Column(String)
    paid = Column(Boolean, default=False)

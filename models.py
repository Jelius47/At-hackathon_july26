from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    plots = relationship('Plot', back_populates='owner')



class Drone(Base):
    __tablename__ = 'drones'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

    plots = relationship('Plot', back_populates='drone')


class Plot(Base):
    __tablename__ = 'plots'

    id = Column(Integer, primary_key=True, index=True)
    size_in_acres = Column(Float, nullable=False)
    number_of_drones = Column(Integer, default=1)

    user_id = Column(Integer, ForeignKey('users.id'))
    drone_id = Column(Integer, ForeignKey('drones.id'))

    owner = relationship('User', back_populates='plots')
    drone = relationship('Drone', back_populates='plots')

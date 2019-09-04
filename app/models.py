from app import db  
from sqlalchemy.orm import relationship

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    photo = db.Column(db.String(128))
    description = db.Column(db.String(128))
    maxPax = db.Column(db.Integer)
    vouchers = relationship("Voucher", back_populates="events") 
    
class Voucher(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True)
    voucher = db.Column(db.String(128))
    dateUsed = db.Column(db.Date) 
    maxPax = db.Column(db.Integer)
    name = db.Column(db.String(128))
    isUploaded = db.Column(db.Integer, default=0)
    numOfDays = db.Column(db.Integer, default=0)
    dayUsed = db.Column(db.Integer, default=0)
    usedPax = db.Column(db.Integer, default=0)
    events_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    events_day = db.Column(db.Date)
    type = db.Column(db.String(128))
    email = db.Column(db.String(60), index=True, unique=True) 
    events = relationship("Event", back_populates="vouchers") 
    claims = relationship("Claim", back_populates="vouchers")

class Claim(db.Model):
    __tablename__ = 'claims'
    id = db.Column(db.Integer, primary_key=True)
    vouchers_id = db.Column(db.Integer, db.ForeignKey('vouchers.id'))
    pax = db.Column(db.Integer)
    status = db.Column(db.Integer)
    vouchers = relationship("Voucher",back_populates="claims")

class Response(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key=True)
    vouchers_id = db.Column(db.Integer, db.ForeignKey('vouchers.id'))
    description = db.Column(db.String(128))
    status = db.Column(db.Integer)
    timestamp = db.Column(db.TIMESTAMP)
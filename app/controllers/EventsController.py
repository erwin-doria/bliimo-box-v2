from flask import session, jsonify
from app.helpers.API import API
from app import db
from app.models import Event, Voucher
from app.schema import event_schema, events_schema
from sqlalchemy import or_

class EventsController:

    def __init__(self, authorization):
        self.authorization = authorization

    def download(self):
        resp = API(self.authorization).downloadEvents()
        data = resp.json()['data']
        events = {}
        
        for event in data:
            eventObj = Event(
                id = event['id'],
                title = event['title'],
                photo = 'no-photo',
                description = event['description'],
                maxPax = event['displayMaxPax'])
                
            events.update({event['id']: eventObj})

        for each in Event.query.filter(Event.id.in_(events.keys())).all():
            db.session.merge(events.pop(each.id))

        db.session.add_all(events.values())
        db.session.commit()
            
        return jsonify(data)
    
    @staticmethod
    def showById(id):
        event = Event.query.filter(Event.id == id).first()
        return event_schema.dump(event)

    @staticmethod
    def showAll(search):
        events = Event.query.filter(or_(Event.title.ilike("%{}%".format(search)), Event.description.ilike("%{}%".format(search)))).all()
        return events_schema.dump(events)
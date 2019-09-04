from app import db
import time
import datetime
from app.models import Response
from app.schema import response_schema
from flask import jsonify
from sqlalchemy import desc
from app.helpers.Dates import timestampNow

class ResponseController:

    @staticmethod
    def add(vouchers_id, description, status):
        respObj = Response(
            vouchers_id = vouchers_id,
            description = description,
            status = status,
            timestamp = timestampNow())

        db.session.add(respObj)
        db.session.commit()
    
    @staticmethod
    def show():
        response = Response.query.order_by(desc(Response.id)).first()
        return jsonify(response_schema.dump(response))
    
    @staticmethod
    def delete(id):
        response = Response.query.filter(Response.id == id).delete()
        db.session.commit()
        return jsonify(response_schema.dump(response))
        
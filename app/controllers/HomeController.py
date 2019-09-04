from flask import jsonify
from app.helpers.API import API
class HomeController:

    @staticmethod
    def login(credentials):
        resp = API({}).login(credentials)
        data = resp.json()
        return jsonify(resp.json())
        

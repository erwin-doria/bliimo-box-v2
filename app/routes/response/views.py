from flask import request
from app.controllers.ResponseController import ResponseController
from . import response


@response.route('/response')
def show():
    return ResponseController.show()

@response.route('/response/delete', methods=['POST'])
def delete(): 
    return ResponseController.delete(request.json['id'])
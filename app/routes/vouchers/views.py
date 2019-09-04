from flask import render_template, request
from . import vouchers
from app.controllers.VouchersController import VouchersController 
from app.controllers.ClaimController import ClaimController 

@vouchers.route('/voucher/<code>')
def scan(code):
    return VouchersController.showByCode(code)

@vouchers.route('/voucher/<code>/<pax>')
def add(code, pax):
    return ClaimController.add(code, int(pax))

@vouchers.route('/voucher/upload', methods=['POST'])
def upload():
    auth = {'Authorization': request.headers['Authorization']}
    return VouchersController(auth).upload()

@vouchers.route('/voucher/refresh', methods=['POST'])
def refresh():
    return VouchersController({}).refresh()
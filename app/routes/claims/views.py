from flask import render_template, request
from app.controllers.ClaimController import ClaimController
from . import claims


@claims.route('/claims', methods=['GET','POST'])
def claim():
    if request.method == 'GET': 
        return render_template('claims/index.html', title="Distribution of tickets")

    elif request.method == 'POST':
        return ClaimController.showAll()

@claims.route('/claim/vouchers', methods=['POST'])
def claimVouchers(): 
    return ClaimController.claim(request.json['id'])

@claims.route('/claim/delete', methods=['DELETE'])
def delete():
    return ClaimController.delete(request.json['id'])

@claims.route('/claim/unredeemed', methods=['GET'])
def unredeemed():
    return ClaimController.showClaimByStatus(0)
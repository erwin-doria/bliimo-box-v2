import json

from flask import session, jsonify
from app.helpers.API import API
from app import db
from app.models import Voucher, Claim
from app.schema import voucher_schema, claims_schema, claim_schema
from sqlalchemy import func 
from .ResponseController import ResponseController
from .VouchersController import VouchersController

class ClaimController:
    def __init__(self, authorization):
        self.authorization = authorization

    @staticmethod
    def add(code, pax):
        voucher = Voucher.query.filter(Voucher.voucher == code).first() 
        if(voucher == None):
            msg = 'Voucher does not exists!'
            ResponseController.add(None, msg, 0)
            return jsonify(msg)

        availablePax = voucher.maxPax - voucher.usedPax
        isSuccess = 0
        claimedPax = 0

        if(voucher != None):
            claimedPax = db.session.query(func.sum(Claim.pax)).filter(Claim.vouchers_id == voucher.id).scalar()
            if(claimedPax == None):
                claimedPax = 0

        if(voucher.usedPax == voucher.maxPax):
            msg = 'Voucher already redeemed!'

        elif(availablePax >= pax): 
            needToClaim = claimedPax + pax 
            
            if (needToClaim <= voucher.maxPax):
                claim = Claim(vouchers_id = voucher.id, pax = pax, status = 0)
                db.session.add(claim)
                db.session.commit()  
                isSuccess = 1

                if(needToClaim == voucher.maxPax):
                    msg = 'Successfully redeemed all vouchers'

                else:
                    msg = 'Successfully redeemed!'

            else:
                msg = 'Voucher already redeemed!' 

        else:
            msg = 'Insuficient pax! Available pax for this voucher is only {}'.format(availablePax - claimedPax) 
        
        ResponseController.add(voucher.id, msg, isSuccess)

        return jsonify(msg)

    @staticmethod
    def showAll():
        claims = Claim.query.all()
        data = claims_schema.dump(claims)
        resp = []
        for i in range(len(data)):
            actions = '' 
            if(data[i]['status'] == 0):
                actions = '<div class="action-btn-claim">'
                actions = actions + '<button class="btn btn-md btn-theme font-weight-bold" onclick="claim({})">Claim</button>'.format(data[i]['id'])
                actions = actions + '<button class="btn btn-md btn-danger font-weight-bold" onclick="deleteClaims({})">Remove</button>'.format(data[i]['id'])
                actions = actions + '</div>'
            else:
                actions = '<span class="text-dark">Claimed</span>'
            data[i]['actions'] = actions

        return jsonify({'data':data})

    @staticmethod
    def claim(id):
        claim = Claim.query.filter(Claim.id == id).first()
        if(claim != None):
            claim.status = 1
            db.session.flush()
            db.session.commit()
            ResponseController.add(None, 'Successfully claimed vouchers', 1)
            VouchersController.setUsedPax(claim)

        return jsonify(claim_schema.dump(claim))

    @staticmethod
    def delete(id):
        claim = Claim.query.filter(Claim.id == id).delete()
        db.session.commit()
        return jsonify(claim_schema.dump(claim))

    @staticmethod
    def showClaimByStatus(status):
        claims = Claim.query.filter(Claim.status == status).all()
        return jsonify(claim_schema.dump(claims))
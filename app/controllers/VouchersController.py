import json

from flask import jsonify
from app.helpers.API import API
from app import db
from app.models import Voucher, Event
from app.schema import voucher_schema, vouchers_schema
from app.helpers.Dates import timestampNow, dateNow, dateFormat, dateDiff
from app.helpers.API import API
from sqlalchemy import func, text
from .ResponseController import ResponseController


class VouchersController:
    def __init__(self, authorization):
        self.authorization = authorization

    def download(self, req):
        resp = API(self.authorization).downloadVouchers(req['id'])
        data = resp.json()['vouchers']
        vouchers = {} 
        if(int(req['isRemoveOld']) == 1):
            Voucher.query.delete()
            db.session.commit()

        for voucher in data:
            if voucher['redemptionStatus'] == 'UNREDEEMED': 
                voucherObj = Voucher(
                voucher = voucher['voucherCode'], 
                maxPax = voucher['totalQuantity'],
                name = "{} {}".format(voucher['owner']['firstName'], voucher['owner']['lastName']),
                isUploaded = 0,
                usedPax = 0,
                numOfDays = 1,
                dayUsed = 0,
                events_id = req['id'],
                events_day = voucher['reservationDate'].split('T')[0],
                type = voucher['passType']) 

                vouchers.update({voucher['voucherCode']:voucherObj})

        for each in Voucher.query.filter(Voucher.voucher.in_(vouchers.keys())).all(): 
            vouchers.pop(each.voucher)

        db.session.add_all(vouchers.values())
        db.session.commit()
            
        return jsonify(vouchers_schema.dump(vouchers.values()))

    def updateUploaded(self, vouchers):
        for i in range(0, len(vouchers)):
            voucher = Voucher.query.filter(Voucher.voucher == vouchers[i]).first()
            if(voucher != None):
                voucher.isUploaded = 1
                db.session.flush()
                db.session.commit()

    def upload(self):
        vouchers = vouchers_schema.dump(Voucher.query.filter(Voucher.maxPax == Voucher.usedPax).filter(Voucher.isUploaded == 0).all())
        voucherCodes = []

        for i in range(0, len(vouchers)):
            voucherCodes.append(vouchers[i]['voucher'])
        
        if(len(voucherCodes) > 0):
            resp = API(self.authorization).uploadVouchers({'codes': voucherCodes}).json()
            if(len(resp['redeemed voucher codes']) > 0):
                self.updateUploaded(resp['redeemed voucher codes'])

        return jsonify(voucherCodes)

    def updateRefreshed(self, voucher):
        voucher.dateUsed = None
        voucher.usedPax = 0
        voucher.isUploaded = 0
        voucher.dayUsed = voucher.dayUsed + 1
        if(voucher.dayUsed == voucher.numOfDays):
            voucher.dateUsed = dateNow()

        db.session.flush()
        db.session.commit()

    def refresh(self):
        vouchers = Voucher.query.filter(Voucher.numOfDays > 1).filter(Voucher.numOfDays > Voucher.dayUsed).filter(Voucher.dateUsed != None).filter(dateFormat(dateNow(),'%Y-%m-%d') >= Voucher.events_day).all()
        vouchersNeedToRefresh = []

        for voucher in vouchers:
            days = dateDiff(dateFormat(dateNow(),'%Y-%m-%d'), voucher.events_day)
            dayUsed = dateDiff(voucher.dateUsed - voucher.events_day)

            if(voucher.numOfDays >= days and dayUsed < voucher.numOfDays):
                self.updateRefreshed(voucher)
                vouchersNeedToRefresh.append(voucher_schema.dump(voucher))

        return jsonify(vouchersNeedToRefresh)

    @staticmethod
    def showByCode(code):
        voucher = Voucher.query.filter(Voucher.voucher == code).first()
        if voucher != None:
            if dateDiff(dateFormat(dateNow(),'%Y-%m-%d'), voucher.events_day) > 1:
                resp = 'Voucher already expired!'
            elif voucher.usedPax == voucher.maxPax:
                resp = 'Voucher already redeemed!'
            else:
                resp = voucher_schema.dump(voucher)
        else:
            resp = 'Voucher does not exists!'
        
        if (type(resp) == str):
            ResponseController.add(None, resp , 0)

        return jsonify(resp)

    @staticmethod
    def setUsedPax(claim):
        voucher = Voucher.query.filter(Voucher.id == claim.vouchers.id).first() 
        totalPax = voucher.usedPax + claim.pax
        voucher.usedPax = totalPax

        if(voucher.maxPax == totalPax): 
            voucher.dateUsed = timestampNow()
        
        db.session.flush()
        db.session.commit()

        return voucher

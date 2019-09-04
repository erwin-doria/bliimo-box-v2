from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    photo = fields.String() 
    maxPax = fields.Integer()  
    vouchers = fields.Nested('VoucherSchema', many = True)

class VoucherSchema(Schema): 
    id = fields.Integer()
    voucher = fields.String()
    dateUsed = fields.Date()
    maxPax = fields.Integer()
    name = fields.String()
    isUploaded = fields.Integer()
    numOfDays = fields.Integer()
    dayUsed = fields.Integer()
    usedPax = fields.Integer()
    events_id = fields.Integer()
    events_day = fields.Date()
    type = fields.String()
    email = fields.Email() 

class ResponseSchema(Schema):
    id = fields.Integer()
    vouchers_id = fields.Integer()
    description = fields.String()
    status = fields.Integer() 
    timestamp = fields.String()  

class ClaimSchema(Schema):
    id = fields.Integer()
    vouchers_id = fields.Integer()
    pax = fields.Integer()
    status = fields.Integer() 
    vouchers = fields.Nested('VoucherSchema')

event_schema = EventSchema()
events_schema = EventSchema(many=True) 

voucher_schema = VoucherSchema()
vouchers_schema = VoucherSchema(many=True)

response_schema = ResponseSchema()
responses_schema = ResponseSchema(many=True)

claim_schema = ClaimSchema()
claims_schema = ClaimSchema(many=True)
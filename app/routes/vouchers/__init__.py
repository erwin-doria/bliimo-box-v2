from flask import Blueprint

vouchers = Blueprint('vouchers', __name__)

from . import views
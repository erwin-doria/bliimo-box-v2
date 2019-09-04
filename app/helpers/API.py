
from flask import session
from pathlib import Path
from PIL import Image
import requests
import socket
import netifaces as ni
import platform

from instance.config import API_BASE_URL

class API:

    def __init__(self, authorization):
        self.headers = { 'Content-Type': 'application/json' }
        self.headers.update(authorization)
    
    def url(self,url): 
        return API_BASE_URL+url

    def login(self, credentials): 
        return requests.post(url = self.url('/login'),headers = self.headers, json = credentials)
    
    def downloadVouchers(self, id):   
        return requests.get(url = self.url('/contents/{}/vouchers?offset=0&limit=1000'.format(id)), headers = self.headers)

    def downloadEvents(self):
        return requests.get(url = self.url('/events?offset=0&limit=100'), headers = self.headers)

    def uploadVouchers(self, vouchers):
        return requests.put(url = self.url('/bliimobox/redeem'), headers = self.headers, json = vouchers)
import os

from app import create_app
from gevent.pywsgi import WSGIServer
from app.helpers.IpAddress import IpAddress 
from instance.config import PORT
app = create_app()

if __name__ == "__main__": 
    app.debug = True 
    http_server = WSGIServer(('192.168.1.35', PORT), app)
    http_server.serve_forever()
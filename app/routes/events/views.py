from flask import render_template, request, jsonify, redirect
from . import events
from app.controllers.VouchersController import VouchersController
from app.controllers.EventsController import EventsController

@events.route('/events/<id>', methods=['GET','POST'])
def event(id):
    if request.method == 'GET': 
        events = EventsController.showById(id) 
        if(bool(events)):
            return render_template('events/event.html', title="Events", events = events)
        else:
            return redirect('/events')

    elif request.method == 'POST': 
        auth = {'Authorization': request.headers['Authorization']}
        data = request.json
        return VouchersController(auth).download(data)


@events.route('/events/search', methods=['POST'])
def eventSearch():
    search = request.json['search']
    return jsonify(EventsController.showAll(search))

@events.route('/events', methods=['GET','POST'])
def events(): 
    if request.method == 'GET':
        events = EventsController.showAll('')
        return render_template('events/index.html', title="Events",len = len(events) ,events = events)
        
    elif request.method == 'POST':
        auth = {'Authorization': request.headers['Authorization']}
        EventsController(auth).download()
        events = EventsController.showAll('')
        return jsonify(events)


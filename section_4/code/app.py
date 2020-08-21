from flask import Flask, request 
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required 

from security import authenticate, identity

app = Flask(__name__)

app.secret_key = 'jose'

api = Api(app)

# JWT creates a new endpoint /auth -> sent username and password 
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
	@jwt_required()
	def get(self, name):
		# Gives first item found by this filter function 
		# filter function takes two arguments, 1 filtering function, 2 list of items you want to filter 
		# go through each item execute this function and see if the items name x name matches -> return 
		item = next(filter(lambda x: x['name'] == name, items), None) # Does item named x match the parameter 
		return {'item' : item}, 200 if item else 404 # 200 if item exists if not 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': "An item with that name '{}' already exists.".format(name)}, 400

		data = request.get_json()  # force=True, silent=True ( optional )
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201


class ItemList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	# look in the list and retrieve the item that matches with the name that has been requested
	def get(self, name):
		for item in items: 
			if item['name'] == name:
				return item 


	def post(self, name):
		item = {'name' : name, 'price': 12.00}
		items.append(item)
		return item

api.add_resource(Item, '/item/<string:name>') 

app.run(port=5000)

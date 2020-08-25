import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type = float,
		required = True,
		help = "This field cannot be left blank!"
	)

	@jwt_required()
	def get(self, name):
		item = self.find_by_name(name)
		if item: 
			return item
		return {'message': 'item not found'}, 404	

	# Error first 
	def post(self, name):
		if self.find_by_name(name):
			return {'message': "An item with name '{}' already exists.".format(name)}, 400

		data = Item.parser.parse_args()

		item = {'name' : name, 'price': data['price']}
		
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES (?, ?)"
		cursor.execute(query, (item))
		return item, 201

	def delete(self, name):
		global items
		# the DB items = result of lambda -> loop through items add every entry where item's name is not = to the name passed in 
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	# The API will not accept any other argument besides price even if they exist inside payload
	def put(self, name):
		
		data = Item.parser.parse_args()

		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else: 
			item.update(data)
		return item

	@classmethod
	def find_by_name(cls, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM items WHERE name=?"
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		connection.close()

class ItemList(Resource):
	def get(self):
		return {'items': items}


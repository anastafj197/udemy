from flask import Flask, jsonify  

app = Flask(__name__)

stores = [
	{
		'name'  : 'My wonderful Store',
		'items' : [
			{
			'name'  : 'My Item',
			'price' : 15.99
			}
		]
	}
]

# POST - used to recieve data 
# GET  - used to send data back only 

# POST /store data: {name:}
@app.route('/store', method=['POST'])
def create_store():
	pass

# GET  /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name' 
def get_store(name)
	pass

# GET /store
@app.route('/store')
def get_stores():
	pass

# POST  /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', method=['POST']) # 'http://127.0.0.1:5000/store/some_name' 
def create_item_in_store(name)
	pass

# GET  /store/<string:name>/item
@app.route('/store/<string:name>/item') 
def get_item_in_store(name)
	pass

app.run(port=5000)
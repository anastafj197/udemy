from user import User
from werkzeug.security import safe_str_cmp

users = [
	User(1, 'bob', 'asdf')
]

# I want an index on bob
username_mapping = { u.username: u for u in users }

# Another instance with the id as the key 
userid_mapping = { u.id: u for u in users }


def authenticate(username, password):
	user = username_mapping.get(username, None)
	if user and safe_str_cmp(user.password, password): 
		return user

def identity(payload):
	userid = payload['identity']
	return userid_mapping.get(user_id, None)
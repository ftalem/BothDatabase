from flask import Flask
from flask.ext.pymongo import PyMongo
from redis import Redis

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flmdb'
app.config['MONGO_URI'] = 'mongodb://addmin:addmin@ds013414.mlab.com:13414/flmdb'

mongo = PyMongo(app)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name' : 'fitu', 'language' : 'python'})
	user.insert({'name' : 'matu', 'language' : 'c'})
	user.insert({'name' : 'katu', 'language' : 'java'})
	user.insert({'name' : 'situ', 'language' : 'c++'})
	user.insert({'name' : 'mitun', 'language' : 'c'})
	return 'added user!'

@app.route('/find')
def find():
	user = mongo.db.users
	cedric = user.find_one({'name' : 'fitu'})
	return 'You found' + cedric['name'] + '. His fav language is' + cedric['language']

@app.route('/update')
def update():
	user = mongo.db.users
	john = user.find_one({'name' : 'fitu'})
	john['language'] = 'javascript'
	user.save(john)
	return 'updated you mf'

@app.route('/delete')
def delete():
	user = mongo.db.users
	kelly = user.find_one({'name' : 'situ'})
	user.remove(kelly)
	return 'As you wish'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
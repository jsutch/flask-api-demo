from flask import Flask

app = Flask(__name__)

# from the API perspective:
# POST - used to recieve data from client
# GET - used to send data to client

# Need a datastore - 
# first round use a nested list of dictionaries
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# Will create:
# POST /store data: (name) - will create a new store with a given name
@app.route('/store',methods=['POST'])
def create_store():
    pass

# GET /store /<string:name>  - get a store for a given name and return data about it
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    pass

# GET /store - return a list of all the stores
@app.route('/store',methods=['GET'])
def get_stores():
    pass

# POST /store/<string:name>/item  (name:price) - create an item inside a specific store with a given name
@app.route('/store/<string:name>',methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item - get all the items within a specific store
@app.route('/store/<string:name>',methods=['GET'])
def get_item_in_store(name):
    pass


app.run(port=5000)

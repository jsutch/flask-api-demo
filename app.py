from flask import Flask, jsonify, request

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
        ],
        'name': 'bob',
        'items': [
            {
                'name': 'Chucks',
                'price': 10.11
            }
        ]
    }
]

# Will create:
# POST /store data: (name) - will create a new store with a given name
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store /<string:name>  - get a store for a given name and return data about it
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    """
    Iterate over stores. If name matches, return store.
    If no match, return error
    """
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    #    else:
    #        return "Not Found"
    return jsonify({'message':'store not found'})

# GET /store - return a list of all the stores
@app.route('/store',methods=['GET'])
def get_stores():
    return jsonify({'stores':stores}) # This converts the list 'stores' into a dictionary 'stores', which can be returned as a json object

# POST /store/<string:name>/item  (name:price) - create an item inside a specific store with a given name
@app.route('/store/<string:name>',methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if name == store['name']:
                request_data = request.get_json()
                new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
                }
        store['name'].append(new_item)
        #return jsonify(store) # return complete store
        return jsonify(new_item) # only return new item
    return jsonify({'message':'store not found'})

# GET /store/<string:name>/item - get all the items within a specific store
@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['items']})
    #    else:
    #        return "Not Found"
    return jsonify({'message':'store not found'})


app.run(port=5000)

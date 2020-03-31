from flask import Flask

app = Flask(__name__)
# the default for @app,route is a get request and browsers, by default, only make get requests
@app.route('/') # 
def home():
    return "Hello New World!"
app.run(port=5000)

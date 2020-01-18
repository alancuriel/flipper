from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import json



app = Flask(__name__)
Bootstrap(app)


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''
    def default(self, o):
        return json.JSONEncoder.default(self, o)

app.config['MONGO_URI'] = "mongodb+srv://alan:Flipper12345@flipper-l35dy.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
app.json_encoder = JSONEncoder


@app.route('/')
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
                           online_users=online_users)

@app.route('/search')
def search():
	# return 'hello_world'
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import datetime


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_URI'] = "mongodb+srv://alan:Flipper12345@flipper-l35dy.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def index():
    print(mongo.db)
    searches = mongo.db.searches
    search_id = searches.insert({'item': "airpods", 'mpn': "MVN2A", 'ebayavg': 34, 'date': datetime.datetime.utcnow()})
    print(search_id)

    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
                           online_users=online_users)

@app.route('/search', methods=['POST', 'GET'])
def search():
	if request.method == 'POST':
		if request.form['secureSearch'] == "on":
			...
		else:
			...
		print(request.form['query'])
		print(request.form)
	return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)


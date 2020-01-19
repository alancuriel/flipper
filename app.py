from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from ebay import getmpn
from ebayApi import get_sold_items_info
import datetime


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_URI'] = "mongodb+srv://alan:Flipper12345@flipper-l35dy.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
                           online_users=online_users)

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        if 'secureSearch' in request.form:
            mpn = getmpn(request.form['query'])
            ebayinfo = get_sold_items_info(mpn)
            searches = mongo.db.searches
            searches.insert({'item': request.form['query'], 'mpn': mpn, 'ebayavg': ebayinfo['AvgPrice'], 'date': datetime.datetime.utcnow()})
        else:
            ebayinfo = get_sold_items_info(request.form['query'])
            searches = mongo.db.searches
            searches.insert({'item': request.form['query'], 'mpn': '', 'ebayavg': ebayinfo['AvgPrice'],
                             'date': datetime.datetime.utcnow()})
        print(request.form['query'])
        print(request.form)
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)


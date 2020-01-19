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

test = {
	"image":"https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen",
	"price" : "25",
	"description" : ""	
}


@app.route('/')
def index():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
                           online_users=online_users)

@app.route('/search', methods=['POST', 'GET'])
def search():
    # data structures of information
    productName = "swolo"
    ebayImg = "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen"
    ebayImg = "data:image/jpeg;base64,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"
    ebayPrice = "25"
    mercariImages = ["https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen", "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen", "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen"]
    mercariPrices = ["40,30,15"]
    mercariDescrip = ["ugly", "more ugly", "super ugly"]
    lenMercari = len(mercariImages) # length of mercari objects
    return render_template('search.html',productName=productName,ebayImg = ebayImg, ebayPrice=ebayPrice,mercariImages=mercariImages,mercariPrices=mercariPrices,mercariDescrip=mercariDescrip,lenMercari=lenMercari)


    # if request.method == 'POST':
    #     #secure search
    #     if 'secureSearch' in request.form:
    #         mpn = getmpn(request.form['query'])
    #         ebayinfo = get_sold_items_info(mpn)
    #         searches = mongo.db.searches
    #         searches.insert({'item': request.form['query'], 'mpn': mpn, 'ebayavg': ebayinfo['AvgPrice'], 'date': datetime.datetime.utcnow()})
    #     else:
    #         ebayinfo = get_sold_items_info(request.form['query'])
    #         searches = mongo.db.searches
    #         searches.insert({'item': request.form['query'], 'mpn': '', 'ebayavg': ebayinfo['AvgPrice'],
    #                          'date': datetime.datetime.utcnow()})
    #     print(request.form['query'])
    #     print(request.form)


    #     # data structures of information
    #     productName = "swolo"
    #     ebayImg = "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen"
    #     ebayPrice = "25"

    #     mercariImages = ["https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen", "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen", "https://mercari-images.global.ssl.fastly.net/photos/m86893773555_1.jpg?1579372204&w=200&h=200&fitcrop&sharpen"]
    #     mercariPrices = ["40,30,15"]
    #     mercariDescrip = ["ugly", "more ugly", "super ugly"]
    #     lenMercari = len(mercariImages) # length of mercari objects


    #     return render_template('search.html',productName=productName,ebayImg = ebayImg, ebayPrice=ebayPrice,mercariImages=mercariImages,mercariPrices=mercariPrices,mercariDescrip=mercariDescrip,lenMercari=lenMercari)
    # return render_template('search.html')



if __name__ == '__main__':
    app.run(debug=True)


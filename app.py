from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	# return 'hello_world'
    return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
	if request.method == 'POST':
		print(request)
	return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)

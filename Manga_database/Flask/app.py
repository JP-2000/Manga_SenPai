from flask import Flask,request

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def hello_world():
	Query = str(request.args['Query'])
	return Query

if __name__ == '__main__' :
	app.run()

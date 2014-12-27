from flask import Flask
import json
app = Flask(__name__)

cars = [{'color': 'red', 'brand': 'BMW', 'plateNumber': '567hghh', 'id': 1}, {'color': 'blue', 'brand': 'Ford', 'plateNumber': '6776hhgd', 'id': 2}, {'color': 'red', 'brand': 'BMW', 'plateNumber': '6887hhgd', 'id': 3}];

@app.route("/cars",methods=['GET'])
def GET_cars():
	return str(json.dumps(cars))

@app.route("/cars",methods=['POST'])
def POST_cars():
	return str(json.dumps(cars))


if __name__ == "__main__":
	app.debug = True;
    	app.run()

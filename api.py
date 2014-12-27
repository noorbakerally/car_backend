from flask import Flask,request
import json
app = Flask(__name__)

cars = [{'color': 'red', 'brand': 'BMW', 'plateNumber': '567hghh', 'id': 1}, {'color': 'blue', 'brand': 'Ford', 'plateNumber': '6776hhgd', 'id': 2}, {'color': 'red', 'brand': 'BMW', 'plateNumber': '6887hhgd', 'id': 3}];

@app.route("/cars",methods=['GET'])
def GET_cars():
	return str(json.dumps(cars))

@app.route("/cars",methods=['POST'])
def POST_cars():
	args = json.loads(request.data)
	newCar = {}
	newCar['color'] = args['color'] 
	newCar['brand'] = args['brand']
	newCar['plateNumber'] =  args['plateNumber']
	newCar['id'] = len(cars)
	cars.append(newCar)
	return str(json.dumps(newCar))

if __name__ == "__main__":
	app.debug = True;
    	app.run()

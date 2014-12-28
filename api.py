from flask import Flask,request
import json
from cross_origin import crossdomain
app = Flask(__name__)

cars = [{'color': 'red', 'brand': 'BMW', 'plateNumber': '567hghh', 'id': 1}, {'color': 'blue', 'brand': 'Ford', 'plateNumber': '6776hhgd', 'id': 2}, {'color': 'red', 'brand': 'BMW', 'plateNumber': '6887hhgd', 'id': 3}]

@app.route("/cars/<car_id>",methods=['GET'])
@crossdomain(origin='*')
def GET_specific_cars(car_id):
	for i in range(len(cars)):
                if (str(cars[i]['id']) == str(car_id)):
			return_obj = {}
			return_obj['car'] = cars[i]
                        return str(json.dumps(return_obj))
        return "id doesn't exist"


@app.route("/cars",methods=['GET'])
@crossdomain(origin='*')
def GET_cars():
	return_obj = {}
	return_obj['cars'] = cars
	return str(json.dumps(return_obj))

@app.route("/cars",methods=['POST'])
@crossdomain(origin='*')
def POST_cars():
	args = json.loads(request.data)
	newCar = {}
	newCar['color'] = args['color'] 
	newCar['brand'] = args['brand']
	newCar['plateNumber'] =  args['plateNumber']
	newCar['id'] = len(cars)
	cars.append(newCar)
	return str(json.dumps(newCar))

@app.route("/cars/<car_id>",methods=['DELETE'])
@crossdomain(origin='*')
def DELETE_cars(car_id):
	for i in range(len(cars)):
		if (str(cars[i]['id']) == str(car_id)):
			del cars[i] 
			return "deleted"
	return "id doesn't exist"
	

@app.route("/cars/<car_id>",methods=['PUT'])
@crossdomain(origin='*')
def UPDATE_cars(car_id):
	args = json.loads(request.data)
	for i in range(len(cars)):
                if (str(cars[i]['id']) == str(car_id)):
			cars[i]['color'] = args['color']
        		cars[i]['brand'] = args['brand']
        		cars[i]['plateNumber'] =  args['plateNumber']
			return str(json.dumps(cars[i]))
	return "id doesn't exist"	
	

if __name__ == "__main__":
	app.debug = True;
    	app.run()

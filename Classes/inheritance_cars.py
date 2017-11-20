class Car(object):
	def __init__(self,make,model):
		self.make = make
		self.model = model

	def start(self):
		print("Starting the gas car")

class electricCar(Car):
	def __init__(self):
		super(electricCar,self).__init__('Tesla','X')

	def start(self):
		print("Starting the electric car!").    # Ovr rides the parent/super class's start function

electric_car = electricCar()
print(electric_car.make)
print(electric_car.model)
electric_car.start().   # Overrides the parents start
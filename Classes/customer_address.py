class Address(object):
	def __init__(self,street,state,zipCode):
		self.street = street
		self.state = state
		self.zipCode = zipCode

class Customer(object):
	def __init__(self):
		self.firstName = ""
		self.lastName = ""
		self.addresses = []   #Create an array is the customer has many addresses.

# Creating A Custoemr
customer = Customer()
customer.firstName = "John"
customer.lastName = "Doe"

# Creating Addresses
address1 = Address("10222 Bellaire", "TX", "77083")
address2 = Address("1500 Katy Fwy", "TX", "77084")
address3 = Address("1200 Richmond Ave", "TX", "77084")
# address1.street = "1200 Richmond Ave"
# adress1.state - "TX"
# address1.zip = "77042"

customer.addresses.append(address1)  # will add
customer.addresses.append(address2)
customer.addresses.append(address3)

print(customer.firstName + " " + customer.lastName)

for address in customer.addresses:
	print(address.street + " " + address.state)
	print("\n")

class Job(object):
	def __init__(self):
		self.title = ""
		self.location = ""
		self.department = ""



class Employee(object):
	def __init__(self,first_name,last_name):
		self.firstName = first_name
		self.lastName = last_name
		self.job = Job() # Here you are inheriting the "Job" parent class into another parent class with the object "job".

employee = Employee("John","Doe")
employee.job.title = "Mechanic"
employee.job.location = "Houston"
employee.job.department = "IT"

print(employee.firstName + " " + employee.lastName)
print(employee.job.title + " " + employee.job.location)
print(employee.job.department)
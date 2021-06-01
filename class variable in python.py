#static variables

class Employee:
    dept = 'Information technology'

    def __init__(self, name, id):
        self.name = name
        self.id = id



emp1 = Employee('John', 'E101')
emp2 = Employee('Marcus', 'E105')

print(emp1.dept)
print(emp2.dept)
print(emp1.name)
print(emp2.name)
print(emp1.id)
print(emp2.id)


print(Employee.dept)  # print the department


emp1.dept = 'Networking'
print(emp1.dept)
print(emp2.dept)

Employee.dept = 'Database Administration'
print(emp1.dept)
print(emp2.dept)

# instance variable

class CoffeeOrder:
	def __init__(self, coffee_name, price):
		self.coffee_name = coffee_name
		self.price = price

customer_order = CoffeeOrder("Espresso", 2.10)
print(customer_order.coffee_name)
print(customer_order.price)

#static methods

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)


print(Person.isAdult(22))

#instance methods

class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

        # Sample Method

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('sree hari')
p.say_hi()

# main method

print("sree")



def main():
    print("hari")



if __name__ == "__main__":
    main()

    
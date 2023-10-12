
from Employees import Employee, Hourly_Employee, Manager
import sys

Rachel = Hourly_Employee("Rachel", 18, "Cashier", wage = 15)

Jeremy = Hourly_Employee("Jeremy", 20, "Cook", wage = 20)

Steven = Manager("Steven", 30, "Head Manager", salary = 50000)

Steven.add_employee(Rachel)

Steven.add_employee(Steven)

for x in Steven.managed_employees:
    print(x.name, "is an employee that works for Steven")

Rachel.add_hours(40)
Rachel.add_commission(3000)
Jeremy.add_hours(48)



#Steven.pay_out()
#Rachel.pay_out()
#Rachel.pay_out()
#Jeremy.pay_out()
#Jeremy.pay_out()

print("Pay ", Steven.name, " $", Steven.pay_out(), ".", sep = '') # pay_out on an manager
print("Pay ", Rachel.name, " $", Rachel.pay_out(), ".", sep = '') # pay_out on an hourly employee wtih commission
print("Pay ", Rachel.name, " $", Rachel.pay_out(), ".", sep = '')
print("Pay ", Jeremy.name, " $", Jeremy.pay_out(), ".", sep = '') # pay_out on an hourly employee with no commission
print("Pay ", Jeremy.name, " $", Jeremy.pay_out(), ".", sep = '')
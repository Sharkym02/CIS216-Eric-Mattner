#   This file contains 3 classes: Employee, Hourly_Employee, and Manager
#   All employees have a name, age, position and payroll, and can be paid out at any time
#
#   Hourly Employees have a set wage, and have their hours worked tracked
#
#   Managers have a salary, and are paid based on that salary and number of employees they manage
#

import sys

class Employee:

    def __init__(self, name, age, position, payroll=0) -> None:
        self.name = str(name)
        self._age = int(age)
        self._position = str(position)
        self._payroll = float(payroll)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        self.position = position
    
    @property
    def payroll(self):
        return self._payroll
    
    @payroll.setter
    def payroll(self, payroll):
        self._payroll = payroll

# This function returns the amount of money the employee should be paid calculated using their wage, salary, number of employees managed, and/or commission
    def pay_out(self):
        if isinstance(self, Hourly_Employee):
            self._payroll += self.wage * self._hours_worked
        elif isinstance(self, Manager):
            for x in self.managed_employees:
                self._payroll += self.salary
        paid = self._payroll
        self._payroll = 0
        self._hours_worked = 0
        return paid

class Hourly_Employee(Employee):

    def __init__(self, name, age, position, wage, payroll=0, hours_worked=0) -> None:
        super().__init__(name, age, position, payroll)
        self.wage = int(wage)
        self._hours_worked = int(hours_worked)

# This function adds a number of hours worked to an employee's record
    def add_hours(self, hours):
        self._hours_worked += hours

# This function adds an amount of money an employee has earned through commission
    def add_commission(self, sales):
        self.payroll += sales
    
class Manager(Employee):

    def __init__(self, name, age, position, salary, managed_employees = None, payroll=0) -> None:
        super().__init__(name, age, position, payroll)
        self.managed_employees = []
        self.salary = int(salary)

# This function adds an employee that is now being managed by the manager
    def add_employee(self, Employee: Employee):
        self.managed_employees.append(Employee)

print("\n********************\nBEGIN TESTS \n********************\n")

test_1 = Hourly_Employee("John", 20, "Clerk", wage = 10)
test_1.add_hours(10)
assert test_1._hours_worked == 10
print("Hours Worked test Passed")

assert test_1.pay_out() == 100
print("Pay out hourly test passed")

test_2 = Manager("Jerry", 30, "Dude", 100)
test_2.add_employee(test_1)
assert test_2.managed_employees[0] == test_1
print("Set managed employee test Passed")

test_3 = Hourly_Employee("Jane", 20, "Clerk", wage = 10)
test_2.add_employee(test_3)
assert test_2.pay_out() == 200
print("Pay out manager test passed")

print("\n********************\nALL TESTS PASSED \n********************\n")
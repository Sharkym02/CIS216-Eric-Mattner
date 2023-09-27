#
#
#
#
#
#
#
#

import sys

class Employee:

    def __init__(self, name, age, position, payroll) -> None:
        self._name = str(name)
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
        self.payroll = payroll

    

class Hourly_Employee(Employee):

    def __init__(self, name, age, position, payroll, hours) -> None:
        super().__init__(name, age, position, payroll, hours)

    def add_hours(self, hours):
        self.hours += hours

    
class Manger(Employee):

    def __init__(self, name, age, position, payroll, salary) -> None:
        super().__init__(name, age, position, payroll, salary)

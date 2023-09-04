# This class defines an object with bmi, feet, inches, kilograms, meters, and pounds as properties, and 
# contains functions to calculate its BMI in either metric or imperial units, as well as to
# convert metric to imperial units and vice versa

class BMI:
    
    # default constructor
    
    def __init__(self, bmi = 0, feet = 0, inches = 0, kilograms = 0, meters = 0, pounds = 0) -> None:
        self._bmi = float(bmi)
        self._feet = float(feet)
        self._inches = float(inches)
        self._kilograms = float(kilograms)
        self._meters = float(meters)
        self._pounds = float(pounds)
    
    @property
    def bmi(self):
        return self.calculate_us()

    @property
    def feet(self):
        return self._feet
    
    @feet.setter
    def feet(self, value):
        self._feet = value
        self._inches = self.feet_to_inches(self._feet)
        self._meters = self.inches_to_meters(self._feet * 12)
    
    @property
    def inches(self):
        return self._inches
    
    @inches.setter
    def inches(self, value):
        self._inches = value
        self._meters = self._meters + self.inches_to_meters(self._inches)
    
    @property
    def kilograms(self):
        return self._kilograms
    
    @kilograms.setter
    def kilograms(self, value):
        self._kilograms = value
        self._pounds = self.kilograms_to_pounds(self._kilograms)
    
    @property
    def meters(self):
        return self._meters
    
    @meters.setter
    def meters(self, value):
        self._meters = value
        self._inches = self.meters_to_inches(self._meters)
    
    @property
    def pounds(self):
        return self._pounds
    
    @pounds.setter
    def pounds(self, value):
        self._pounds = value
        self._kilograms = self.pounds_to_kilograms(self._pounds)

    def calculate_metric(self):
        return round(self._kilograms
                     / self._meters**2, 1
                     )

    def calculate_us(self):
        return round(703 
                     * self._pounds 
                     / (self._feet * 12 + self._inches)**2, 1
                     )
    
    def feet_to_inches(self, feet):
        return (feet
                * 12
                )
    
    def inches_to_meters(self, inches):
        return (inches
                / 39.37
                )
    
    def kilograms_to_pounds(self, kilograms):
        return (kilograms
                * 2.205
                )
    
    def meters_to_inches(self, meters):
        return (meters
                * 39.37
                )

    def pounds_to_kilograms(self, pounds):
        return (pounds
                * 2.205
                )
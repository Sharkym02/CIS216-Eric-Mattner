# This class defines an object with a height and weight, and contains functions to calculate its BMI in either metric or imperial units

class bmi_calculator:
    
    def __init__(self, weight, height) -> None:
        self.weight = weight
        self.height = height
        
    def calculate_bmi_metric(self):
        return round(self.weight
                     / self.height**2, 1
                    )

    def calculate_bmi_imperial(self):
        return round(703 
                    * self.weight 
                    / self.height**2, 1
                    )
    
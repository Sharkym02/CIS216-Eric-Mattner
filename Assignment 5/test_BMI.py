## This Program Contains Test Cases for each function in BMI.py

from BMI import BMI

def test_set_feet():
    feet = BMI()
    feet.feet = 5
    assert feet.feet == 5

def test_set_inches():
    inches = BMI()
    inches.inches = 60
    assert inches.inches == 60
    assert inches.meters == 60 / 39.37

def test_set_pounds():
    pounds = BMI()
    pounds.pounds = 150
    assert pounds.pounds == 150
    assert pounds.kilograms == 150 / 2.205
    assert pounds.pounds == 150
    assert pounds.kilograms == 150 / 2.205

def test_set_meters():
    meters = BMI()
    meters.meters = 1.8
    assert meters.meters == 1.8
    assert meters.inches == 1.8 * 39.37

def test_set_kilograms():
    kilograms = BMI()
    kilograms.kilograms = 80
    assert kilograms.kilograms == 80
    assert kilograms.pounds == 80 * 2.205

def test_US_inches():
    US = BMI()
    US.inches = 70
    US.pounds = 150
    assert US.calculate_us() == 21.5
    assert US.calculate_metric() == 21.5
    
def test_US_feet():
    US = BMI()
    US.feet = 6
    US.pounds = 150
    assert US.calculate_us() == 20.3
    assert US.calculate_metric() == 20.3

def test_US():
    US = BMI()
    US.feet = 5
    US.inches = 8
    US.pounds = 150
    assert US.calculate_us() == 22.8
    assert US.calculate_metric() == 22.8

def test_metric():
    metric = BMI()
    metric.kilograms = 70
    metric.meters = 1.8
    assert metric.calculate_metric() == 21.6
    assert metric.calculate_us() == 21.6


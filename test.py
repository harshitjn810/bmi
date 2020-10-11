import unittest
import bmi_cal
class Testbmi(unittest.TestCase):
    #Testcase for bmi less than and equals to 18.4
    def test_cal_bmi_underweight(self):
        bmi = bmi_cal.cal_bmi('Male',171,50)
        self.assertListEqual(bmi,[17.1,'Underweight','Malnutrition risk'])

    #Testcase for bmi less than 34.9 and greater than 30
    def test_cal_bmi_moderately_obese(self):
        bmi = bmi_cal.cal_bmi('Male',171,96)
        self.assertListEqual(bmi,[32.8,'Moderately obese','Medium risk'])

    #Testcase for bmi less than 24.9 and greater than 18.5
    def test_cal_bmi_normal_weight(self):
        bmi = bmi_cal.cal_bmi('Female',180,77)
        self.assertListEqual(bmi,[23.8,'Normal weight','Low risk'])

    #Testcase for bmi less than 29.9 and greater than 25
    def test_cal_bmi_overweight(self):
        bmi = bmi_cal.cal_bmi('Female',167,82)
        self.assertListEqual(bmi,[29.4,'Overweight','Enhanced risk'])

    #Testcase for bmi less than 39.9 and greater than 35
    def test_cal_bmi_severely_obese(self):
        
        bmi = bmi_cal.cal_bmi('Female',161,100)
        self.assertListEqual(bmi,[38.6,'Severely obese','High risk'])

    #Testcase for bmi greater than and equals to 40
    def test_cal_bmi_very_severely_obese(self):
        bmi = bmi_cal.cal_bmi('Female',161,150)
        self.assertListEqual(bmi,[57.9,'Very severely obese','Very high risk'])

if __name__=='__main__':
    unittest.main()
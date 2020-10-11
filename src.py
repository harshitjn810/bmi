import json
import bmi_cal

#Read and load the json input from input_json file
file = open('input_json.txt','r')
input_data = file.read()


json_data = json.loads(input_data)
bmi_data=[]
for data in json_data:
    #Calling cal_bmi to calculate the bmi
    bmi_data.append(bmi_cal.cal_bmi(data['Gender'],data['HeightCm'],data['WeightKg']))

#Printing the result    
print(bmi_data)
print('Number of overweighted people are {}'.format(bmi_cal.count))
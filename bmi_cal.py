count = 0

def cal_bmi(gender,heightcm,weightkg):
    global count
    heightm = heightcm/100
    bmi = round(weightkg/(heightm**2),1)
    #print('BMI is {}'.format(bmi))
    if bmi<=18.4:
        bmi_category = 'Underweight'
        health_risk = 'Malnutrition risk'
    elif bmi >= 18.5 and bmi <=24.9:
        bmi_category = 'Normal weight'
        health_risk = 'Low risk'
    elif bmi >= 25 and bmi <=29.9:
        count=count+1
        bmi_category = 'Overweight'
        health_risk = 'Enhanced risk'
    elif bmi >= 30 and bmi <=34.9:
        bmi_category = 'Moderately obese'
        health_risk = 'Medium risk'
    elif bmi >= 35 and bmi <=39.9:
        bmi_category = 'Severely obese'
        health_risk = 'High risk'
    else:
        bmi_category = 'Very severely obese'
        health_risk = 'Very high risk'
    return [bmi,bmi_category,health_risk]

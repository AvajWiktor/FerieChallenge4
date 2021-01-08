
import random
import json
import requests

def get_category(bmi):
        if bmi >= 40: 
            return ["Obese Class III (Very severely obese)", "7"]
        elif bmi >=35:
            return ["Obese Class II (Severely obese)", "6"]
        elif bmi >=30:
            return ["Obese Class I (Moderately obese)", "5"]
        elif bmi>=25:
            return ["Overweight", "4"]
        elif bmi>=18.5:
            return ["Normal (healthy weight)", "3"]
        elif bmi>=16:
            return ["Underweight", "2"]
        elif bmi>=15:
            return ["Severely underweight", "1"]
        elif bmi>=0:
            return ["Very severely underweight", "0"]
class Coach():
    def __init__(self, bmi, bmiType, maxTime):
        self.max_time = maxTime
        self.bmi = int(bmi)
        self.bmi_type = bmiType
        self.exercises = {
                    0:'Running',
                    1:'Pushups',
                    2:'Squats',
                    3:'Pull Ups',
                    4:'Hollow Body',
                    5:'Plank',
                 }
        min_time={
                     0:"15",
                     1:"20",
                     2:"25",
                     3:"30",
                     4:"35",
                     5:"38",
                     6:"40",
                     7:"41",
                  }
        self.min_time=min_time.get(int(bmiType),"Invalid type of trening")

    def create_plan(self):
        time = 0
        exercise_time = (float(self.bmi)**2/(float(self.min_time)**2)) + float(self.min_time)
        if exercise_time > self.max_time:
             time = str(self.max_time)
        else:
             time = "{:.2f}".format(exercise_time)

        temp =[]
        for x in range(7):
            temp.append(str(self.exercises.get(random.randint(0,5),"Invalid type of trening")))
       
        data_set =  "Tranin plan for: "+get_category(self.bmi)[0] +"\nDay1 - Exercise: " +temp[0] + ", Time: " +time+" min" + "\nDay2 - Exercise: " +temp[1] + ", Time: " +time+" min" + "\nDay3 - Exercise: " +temp[2] + ", Time: " +time+" min" + "\nDay4 - Exercise: " +temp[3] + ", Time: " +time+" min" + "\nDay5 - Exercise: " +temp[4] + ", Time: " +time+" min"+ "\nDay6 - Exercise: " +temp[5] + ", Time: " +time+" min" + "\nDay7 - Exercise: " +temp[6] + ", Time: " +time+" min"
        text_file = open("plan.txt", "w")
        n = text_file.write(data_set)
        text_file.close()            

        
    


class BMI():
    def __init__(self):
        mass_kg = float(input("Enter your bodyweight in kg: "))
        height_cm = float(input("Enter your height in cm: "))
        sex = input("Enter your sex: ")
        age = int(input("Enter your age: "))
        self.bmi = mass_kg/((height_cm/100)**2)
        category_array = get_category(self.bmi)

        self.category = int(category_array[1])
        self.category_description = category_array[0]
        self.mass = mass_kg
        self.height = height_cm
        self.sex = sex
        self.age = age

    


user = BMI()
coach = Coach(user.bmi, user.category, int(input("Enter your max time for exercises: ")))
coach.create_plan()
print(user.category_description)













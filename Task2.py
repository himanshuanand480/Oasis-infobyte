weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meter: "))
#create a function 
def BMI(weight,height):
    if weight<=0 or height<=0:
        print("Enter valid data")
    else:
        #use the BMI formula 
        bmi=(weight)/((height)**2)
        print("Your BMI is: ",round(bmi,2))
#use round() function to round the result upto 2 decimal place,we can round the value as per need it may be upto 3 or 4 place
        if bmi<18.5:
            return "Underweight"
        elif 18.5<=bmi<=24.9:
            return"Normal weight"
        elif 25<=bmi<29.9:
            return "Over weight"
        else:
            return "Obese"
print(BMI(weight,height))

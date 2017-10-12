weight=eval(input("Enter weight in pounds:"))
feet=eval(input("Enter feet:"))
inches=eval(input("Enter inches:"))
KILOGRAMS_PER_POUND=0.45359237
METERS_PER_INCH=0.0254
weightInKilograms=weight*KILOGRAMS_PER_POUND
heightInMeters=(feet*12+inches)*METERS_PER_INCH
bmi=weightInKilograms/(heightInMeters*heightInMeters)
print("BMI is",format(bmi,".2f"))
if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")
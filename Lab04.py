#Question1
ques1 = int(input("Enter your age : "))
print(f"You are {ques1} years old.")

#Question2
Hours = int(input("Enter hours: "))
Mins = int(input("Enter minutes: "))
print(f"Time is {Hours}:{Mins}")

#Question3
C = float(input("Enter Celsius: "))
F = ((9/5 * C) + 32)
print (f"{C} Celsius = {F} Farenheit")

#Question4
g = int(input("What is the mass of the object in grams? "))
kg = int(g * 0.001)
gminus = int(kg * 1000)
g = (g - gminus)
print (f"It is approximately {kg} kg, {g} g")

#Question5
Mark1 = float(input("Enter Mark #1: "))
Mark2 = float(input("Enter Mark #2: "))
Avrg = ((Mark1 + Mark2) / 2)
print(Avrg)

#Question 6
from fractions import Fraction
Num1 = int(input("Enter numerator #1: "))
Denom1 = int(input("Enter Denominator #1: "))
Num2 = int(input("Enter numerator #2: "))
Denom2 = int(input("Enter Denominator #1: "))
Calc = Fraction((Num1 / Denom1) + (Num2 / Denom2))
print(Calc)

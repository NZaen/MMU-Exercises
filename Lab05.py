#Question 5
initial_salary = float(input("Enter beginning salary:  RM"))
salary = initial_salary
pay_raise = float(input("Enter pay raise %: "))
years = int(input("How many years? : "))

#Define function for salary calculation
def new_salary():
  global salary
  salary = (salary + (salary * pay_raise/100))

#Loop new_salary() 3 times
for i in range(years):
  new_salary()

#Output Salary after n amount of years
print (f"New salary after {years} years: RM{salary:,.2f}")

#Output Change
change = salary - initial_salary
print(f"Change RM: {change:,.2f}")

#Output Change Percent
change_percent = (change / initial_salary * 100)
print(f"Change % : {change_percent:,.2f}")

#Question 6
principal = int(input("Enter principal : RM "))
interest_rate = int(input("Enter interest rate %: "))
years = int(10)

#Function for salary calculation
def calculation():
  global years
  future_value = (principal * ((1 + interest_rate / 100) ** years))
  print (f"{years} years : RM{future_value:10,.2f}")
  years = (years + 10)


print("Future value after")

#Loop calculation() 6 times
for i in range(6):
  calculation()




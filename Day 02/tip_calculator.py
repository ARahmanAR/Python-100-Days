#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Long process

# tip_percent = tip / 100
# total_tip = total_bill * tip_percent
# total_bill += total_tip
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2) # Rounding the number to 2 decimal places using round method in python. 
# final_amount = "{:.2f}".format(bill_per_person) # Another way to round the number to 2 decimal places using format method in string class in python.
# print(f"Each person should pay: ${final_amount}")

# In short process

tip_percent = tip / 100
total_bill += total_bill * tip_percent
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person) # Another way to round the number to 2 decimal places using format method in string class in python.
print(f"Each person should pay: ${final_amount})
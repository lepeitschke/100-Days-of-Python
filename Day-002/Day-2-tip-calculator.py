#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

welcome_message = "Welcome to the tip calculator."
print(welcome_message)

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

bill_per_person = (bill * (100+tip) / 100) / people
final_amount = round(bill_per_person, 2)  #sometimes there are not enough decimal characters so, it doesn't show enough decimal places e.g. 2.1
# format the number
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")150

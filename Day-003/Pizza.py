print("Welcome to Perfect Pizza Plunder")

size = input("What size should your perfect pizza plunder have? S, M or L? ")
pepperoni =  input("Would you like to add pepperoni? y for Yes and n for No ")
vegan = input("Should your pizza be vegan? y for Yes and n for No ")

if size == "S":
  bill =7
elif size == "M":
  bill = 10
else:
  bill = 11.5

if pepperoni == "y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if vegan == "y":
  print("Congratulations!!! Your pizza will be on the house!!!")
else:
  print("Sorry, go commit die!")

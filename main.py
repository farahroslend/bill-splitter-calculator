bill=input("Enter the total bill cost = ")
numberOfPeople=input("Enter the number of people to split the bill with = ")
tipPercentage=input("Enter the % of the bill you want to leave as tip = ")
#commented out lines are not needed
#print(bill)
#print(numberOfPeople)
#print(tipPercentage)
split=float(bill)*((float(tipPercentage)+100)/100)/int(numberOfPeople)
print(f"Here's the bill split per person : {round(split,2)} ")
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people will split the bill? "))

money = bill + bill * tip/100
final_bill = money/int(people)
word = round(final_bill,2)
print(f"Each person should pay: ${word}")

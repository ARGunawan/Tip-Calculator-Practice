#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

initial_bill = float(input("what was the total bill?\n$"))

tip = int(input("How much tip would you like to give? 10%, 12%, or 15%?\n"))

people = int(input("How many people to split the bill?\n"))

tip_percentage = tip/100
initial_and_tip = tip_percentage * initial_bill
total_bill = initial_bill + initial_and_tip
split = (total_bill/people)
split_person = round(split, 2)
final_amount = "{:.2f}".format(split_person)
print(f"Each person should pay ${final_amount}")






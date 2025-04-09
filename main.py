#Tax Assignment
#Made by Gabriel 

#yearly_inc input by user and the money worth in each tax range

first_bracket = 55867
second_bracket = 117733
third_bracket = 173205
fourth_bracket = 246752

#user is inputting their yearly income

print("Hello, user. Please input your yearly income to do the following calculations: Your tax bracket, your owed taxes, and the average tax rate you pay.")
yearly_inc = float(input("Input your yearly income here: "))

# How it works (pattern)
# if statement:
    # print the bracket
    # (amount of money * tax percentage) + ((yearly income - amount of money){to get the money above the amount of money to be multiplied} * second tax percentage)

if yearly_inc <= first_bracket:
    print("You are in the first bracket (15% tax)")
    tax_owed = yearly_inc * 0.15

elif yearly_inc <= second_bracket:
    print("You are in the second bracket (20.5% tax)")
    tax_owed = (first_bracket * 0.15) + ((yearly_inc - first_bracket) * 0.205)

elif yearly_inc <= third_bracket:
    print("You are in the third bracket (26% tax)")
    tax_owed = (first_bracket * 0.15) + ((second_bracket - first_bracket) * 0.205) + ((yearly_inc - second_bracket) * 0.26)

elif yearly_inc <= fourth_bracket:
    print("You are in the fourth bracket (29% tax)")
    tax_owed = (first_bracket * 0.15) + ((second_bracket - first_bracket) * 0.205) + ((third_bracket - second_bracket) * 0.26) + ((yearly_inc - third_bracket) * 0.29)

else:
    print("You are in the fifth bracket (33% tax)")
    tax_owed = (first_bracket * 0.15) + ((second_bracket - first_bracket) * 0.205) + ((third_bracket - second_bracket) * 0.26) + ((fourth_bracket - third_bracket) * 0.29) + ((yearly_inc - fourth_bracket) * 0.33)

# This takes amount of tax owed and will divide by the yearly income to get the avg tax rate

average_tax_rate = (tax_owed / yearly_inc) * 100

# Bi weekly pay with tax owed

# 26 payments bi-weekly

bi_weekly_pay_untouched = yearly_inc / 26

tax_owed_bi_weekly = tax_owed / 26

true_bi_weekly_payment = bi_weekly_pay_untouched - tax_owed_bi_weekly

# Max EI variable trying to cap it out

max_ei_percentage = 0.164
max_ei = 0
counter = 0

while max_ei != 1077.48:
    max_ei = true_bi_weekly_payment * max_ei_percentage 
    updated_bi_weekly_payment = true_bi_weekly_payment - max_ei
    counter =+ 1
    if max_ei == 1077.48:
        print("You have reached max Eyployment Insurance amount")
        print("it took #put variable of counter here for weeks# amount of weeks to fill up")
        
# EI Calculation (1.64% of gross yearly income, capped at $1077.48)
ei_total = min(yearly_inc * 0.0164, 1077.48)
ei_bi_weekly = ei_total / 26

# Adjust bi-weekly payment after EI deduction
true_bi_weekly_payment_after_ei = true_bi_weekly_payment - ei_bi_weekly

# This will print the necessary information that will be given to the user 

print("----------------------------------------------------------")
print("Your total tax owed is: ${:.2f}".format(tax_owed))
print("----------------------------------------------------------")
print("Your average tax rate is: {:.2f}%".format(average_tax_rate))
print("----------------------------------------------------------")
print("Your bi-weekly payment is: ${:.2f}".format(true_bi_weekly_payment_after_ei))
print("----------------------------------------------------------")
print("Your bi-weekly payment tax is: ${:.2f}".format(tax_owed_bi_weekly))
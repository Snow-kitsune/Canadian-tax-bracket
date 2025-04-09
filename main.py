# Tax Assignment
# Made by Gabriel

# Yearly income brackets (Federal)
first_bracket = 55867
second_bracket = 117733
third_bracket = 173205
fourth_bracket = 246752

# User input
print("Hello, user. Please input your yearly income to do the following calculations: Your tax bracket, your owed taxes, and the average tax rate you pay.")
yearly_inc = float(input("Input your yearly income here: "))

# Tax calculation based on federal brackets
if yearly_inc <= first_bracket:
    print("You are in the first bracket (15% tax)")
    tax_owed = yearly_inc * 0.15

elif yearly_inc <= second_bracket:
    print("You are in the second bracket (20.5% tax)")
    tax_owed = (first_bracket * 0.15) + ((yearly_inc - first_bracket) * 0.205)

elif yearly_inc <= third_bracket:
    print("You are in the third bracket (26% tax)")
    tax_owed = (first_bracket * 0.15) + \
               ((second_bracket - first_bracket) * 0.205) + \
               ((yearly_inc - second_bracket) * 0.26)

elif yearly_inc <= fourth_bracket:
    print("You are in the fourth bracket (29% tax)")
    tax_owed = (first_bracket * 0.15) + \
               ((second_bracket - first_bracket) * 0.205) + \
               ((third_bracket - second_bracket) * 0.26) + \
               ((yearly_inc - third_bracket) * 0.29)

else:
    print("You are in the fifth bracket (33% tax)")
    tax_owed = (first_bracket * 0.15) + \
               ((second_bracket - first_bracket) * 0.205) + \
               ((third_bracket - second_bracket) * 0.26) + \
               ((fourth_bracket - third_bracket) * 0.29) + \
               ((yearly_inc - fourth_bracket) * 0.33)

# Average tax rate
average_tax_rate = (tax_owed / yearly_inc) * 100

# EI Simulation using while loop (1.64% of gross income, capped at $1077.48)

ei_cap = 1077.48
ei_percentage = 0.0164
ei_paid = 0
weeks_counter = 0
gross_bi_weekly = yearly_inc / 26
ei_contributions = []  # Optional: to track each period’s contribution (for extra detail)

while ei_paid < ei_cap:
    contribution = gross_bi_weekly * ei_percentage

    # Prevent going over the cap
    if ei_paid + contribution > ei_cap:
        contribution = ei_cap - ei_paid

    ei_paid += contribution
    ei_contributions.append(contribution)  # For tracking each payment
    weeks_counter += 1

# Final bi-weekly EI deduction (last contribution might be smaller than regular)
ei_bi_weekly = gross_bi_weekly * ei_percentage
true_bi_weekly_payment_after_ei = true_bi_weekly_payment - ei_bi_weekly

# Output
print("----------------------------------------------------------")
print("Your total EI contribution is: ${:.2f}".format(ei_paid))
print("It takes {} bi-weekly payments to reach the EI max of ${:.2f}".format(weeks_counter, ei_cap))
print("Your regular bi-weekly EI deduction is: ${:.2f}".format(ei_bi_weekly))
print("Your final bi-weekly pay after tax and EI: ${:.2f}".format(true_bi_weekly_payment_after_ei))


# Output results
print("----------------------------------------------------------")
print("Your total tax owed is: ${:.2f}".format(tax_owed))
print("----------------------------------------------------------")
print("Your average tax rate is: {:.2f}%".format(average_tax_rate))
print("----------------------------------------------------------")


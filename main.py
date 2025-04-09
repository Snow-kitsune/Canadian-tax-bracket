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

# Bi-weekly pay
bi_weekly_pay_untouched = yearly_inc / 26
tax_owed_bi_weekly = tax_owed / 26
true_bi_weekly_payment = bi_weekly_pay_untouched - tax_owed_bi_weekly

# EI Calculation (1.64% of gross yearly income, capped at $1077.48)
ei_total = min(yearly_inc * 0.0164, 1077.48)
ei_bi_weekly = ei_total / 26
true_bi_weekly_payment_after_ei = true_bi_weekly_payment - ei_bi_weekly

# CPP Calculation (5.95% of gross yearly income, capped at $4034.10
cpp_total = min(yearly_inc * 0.0595, 4034.10)
cpp_bi_weekly = cpp_total / 26
true_bi_weekly_payment_after_ei_and_cpp = true_bi_weekly_payment_after_ei - cpp_bi_weekly

# Output results
print("----------------------------------------------------------")
print("Your total tax owed is: ${:.2f}".format(tax_owed))
print("----------------------------------------------------------")
print("Your average tax rate is: {:.2f}%".format(average_tax_rate))
print("----------------------------------------------------------")
print("Your bi-weekly payment before deductions: ${:.2f}".format(bi_weekly_pay_untouched))
print("Your bi-weekly tax deduction: ${:.2f}".format(tax_owed_bi_weekly))
print("Your bi-weekly EI deduction: ${:.2f}".format(ei_bi_weekly))
print("Your bi-weekly CPP deduction:${:.2f}".format(cpp_bi_weekly))
print("----------------------------------------------------------")
print("Your total EI contribution for the year: ${:.2f}".format(ei_total))
print("Your total CPP contribution for the year: ${:.2f}".format(cpp_total))
print("----------------------------------------------------------")
print("Your bi-weekly pay after all deductions: ${:.2f}".format(true_bi_weekly_payment_after_ei_and_cpp))

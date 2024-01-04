import math

# Display the opening message
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan \n")

# Use a while loop to validate users input == investment or bond
while True:
    calculator_choice = (input("Enter either 'investment' or 'bond' from the menu above to proceed: \n")) # request input from the user, store in variable
    calculator_choice = calculator_choice.lower() # defensive programming to combat against syntax errors
    if calculator_choice not in ('bond', 'investment'): 
        print("Error - please check your spelling and enter investment or bond. Please start again. \n ")
    else: break 
print(f"You have chosen {calculator_choice}. ") # confirm the users input

# Program the investment route
if calculator_choice == 'investment':
    # request the deposit amount
    investment_deposit = (input("Please enter the amount of money you would like to invest: \n"))
    investment_deposit = investment_deposit.replace(",", "").replace("£", "")  # defensive programming against commas used for indicating thousands, as well as £ sign
    investment_deposit = int(investment_deposit)
    # request the interest rate
    investment_interest_rate = int(input("Please enter the interest rate for your investment: \n"))
    # request length of investment
    investment_length = int(input("Please enter the number of years you wish to invest for: \n"))
    # implement  while loop to prompt user to choose simple or compound
    while True:
        interest = input("Please type simple or compound to calculate the respective interest: \n")
        interest = interest.lower()
        if interest not in ('simple', 'compound'):
            print("Error - please check your spelling and enter simple or compound. Please try again. \n")
        elif interest in 'simple': # program the simple interest choice
            simple_interest = investment_deposit * (1 + investment_interest_rate / 100 * investment_length) # Program the simple interest calculation
            simple_interest = int(simple_interest) # cast to integer
            print(f"Your simple interest return would be: {simple_interest}")
            break
        elif interest in 'compound': 
            compound_interest = investment_deposit * math.pow((1 + investment_interest_rate / 100), investment_length) # program compound interest choice and calculation
            compound_interest = int(compound_interest) # cast to integer
            print(f"Your compound interest return would be: {compound_interest}")
            break
        else: break

# program the bond route 
if calculator_choice == 'bond': 
    house_value = input("Please input the house value: \n") # request the house value
    house_value = house_value.replace(",", "").replace("£", "")  # defensive programming against commas used for indicating thousands, as well as £ sign
    house_value = int(house_value)
    # request the bond interest rate
    bond_interest_rate = int((input("Please enter the annual interest rate for your bond: \n")))
    bond_interest_rate = bond_interest_rate / 12 # calculates the monthly interest rate, necessary for final calculation
    # request the time frame for repayment
    bond_repayment_duration = int(input("Please enter the the number of months it will take you to repay the bond: \n"))
    # calculate the bond repayment
    monthly_bond_repayment = (bond_interest_rate * house_value)/(1 - (1 + bond_interest_rate)**(- bond_repayment_duration))
    print(f"Your monthly bond repayment would be: {monthly_bond_repayment}")










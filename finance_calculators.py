#Compulsory Task 1

#Import the math package. 

import math

#Ask the user for what type of calculator they want to use, 'investment' or 'bond' with a description of each.  Convert the response into all lowercase so that the input is not case sensitive. 

calculator_type = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment - to calculate the amount of interest youll earn on your investment\nbond - to calculate the amout you'll have to pay on a home loan\n\nPlease type your choice here: ").lower()

#If/elif statement depending on the calculator_type that the user chose. 
#Investment calculator

if calculator_type == "investment":

    #If the user wants to use the investment calculator, we need to ask them for the following information:
    
    deposit_amount = float(input("What is the amount you are depositing in £? "))   #Deposit amount
    interest_rate_percentage = float(input("What is the interest rate you will receive? "))     #Interest rate as a percentage
    investment_term = float(input("How many years do you plan on investing? "))     #Term of the investment in years
    interest_type = input("Do you want simple or compounding interest? Please type 'compounding' or 'simple' ")     #Calculation method for interest. 
    
    #convert interest rate to decimal for use in further calculations

    interest_rate_decimal = interest_rate_percentage/100  

    #After gathering all of the inputs we want to calculate the total amount including interest at the end of the investment term.  An if/elif statement is written to perform the calculation depending on what method was chosen by the user. 

    if interest_type == "simple":   
        total_amount = round(deposit_amount*(1+interest_rate_decimal*investment_term),2) #Formula for simple interest, rounded to two decimal places
    elif interest_type == "compounding":
        total_amount = round(deposit_amount*math.pow((1+interest_rate_decimal),investment_term),2) #Formula for compounding interest, rounded to two decimal places
    
    #Print a summary of the investment details and the resulting amount at the end of the investment term. 

    print(f"Summary of Investment:\nInvestment amount:\t £{deposit_amount}\nInvestment term:\t{investment_term} years\nInterest rate:\t{interest_rate_percentage}%\nInterest calculation method:\t{interest_type}\nTotal amount with interest applied:\t£{total_amount}")


#Bond calculator

elif calculator_type == "bond":

    #If the user wants to use the bond calculator, we need to ask them for the present value of the house, interest rate and bond term in months. 

    present_value = float(input("What is the present value of the house in £? "))   #Present value of the house. 
    interest_rate_percentage = float(input("What is the interest rate you will receive? "))     #Interest rate percentage
    bond_term = float(input("How months do you plan to take to repay the bond? "))  #Bond term selected by the user. 

    #Monthly interest rate as a decimal, set as a variable as it used twice in the repayment formula to follow. 
   
    monthly_interest_rate_decimal = interest_rate_percentage/(12*100)   

    #With all the inputs from the user we use the repayment formula to calculate the repayment amount for the bond term. The result is rounded to two decimal places. 
    
    monthly_repayment = round(monthly_interest_rate_decimal/(1-(1+monthly_interest_rate_decimal)**(-bond_term)),2)

    #Print a summary of the bond details and the monthly repayment amount. 

    print(f"Summary of Bond Repayment:\nHouse value:\t £{present_value}\nBond term:\t{bond_term} years\nInterest rate:\t{interest_rate_percentage}%\nMonthly Repayment Amount:\t£{monthly_repayment}")



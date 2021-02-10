###Author:Aditya Jadhav
###Course:CSC110
###Description:This program takes 6 inputs from the user rangoing from his annual salary to other expenses
###            (like food,travel and other) and then calculates the tax and the money saved by the user
###            in the whole year. It also warns about budget deficit and if he has reached the income tax limit.


import os
print("-----------------------------")
print("----- WHERE'S THE MONEY -----")
print("-----------------------------")
annual_salary=input("What is your annual salary?\n")    ###This code is taking input from the users about their salary and expenses.
if annual_salary.isnumeric()==False:
    print("Must enter positive integer for salary.")
    os._exit(0)
monthly_mortgage=input("How much is your monthly mortgage or rent?\n")
if monthly_mortgage.isnumeric()==False:
    print("Must enter positive integer for mortgage or rent.")
    os._exit(0)
monthly_bills=input("What do you spend on bills monthly?\n")
if monthly_bills.isnumeric()==False:
    print("Must enter positive integer for bills.")
    os._exit(0)
weekly_food=input("What are your weekly grocery/food expenses?\n")
if weekly_food.isnumeric()==False:
    print("Must enter positive integer for food.")
    os._exit(0)
annual_travel=input("How much do you spend on travel annually?\n")
if annual_travel.isnumeric()==False:
    print("Must enter positive integer for travel.")
    os._exit(0)
###This whole code(from line 32 to 50) is for finding out the TAX amount and TAX percentage.
if float(annual_salary)*(.3)>=75000:     ###This is to find out if TAX limit has been reached
    tax=75000
    tax_percentage=(75000/float(annual_salary))*100
elif float(annual_salary)<=15000 and float(annual_salary)>=0:
    tax=float(annual_salary)*(.1)
    tax_percentage=10
elif float(annual_salary)>15000 and float(annual_salary)<=75000:
    tax=float(annual_salary)*(0.2)
    tax_percentage=20
elif float(annual_salary)>75000 and float(annual_salary)<=200000:
    tax=float(annual_salary)*(.25)
    tax_percentage=25
elif float(annual_salary)>200000:
    tax=float(annual_salary)*30
    tax_percentage=30

extra=(float(annual_salary)-(float(monthly_mortgage)*12)-(float(monthly_bills)*12)-(float(weekly_food)*52)-float(annual_travel)-float(tax))
###In the below code we multiply expenses by 12 for monthly expenses and by 52 for weekly expenses to make them annual expense
mortgage_percentage=(float(monthly_mortgage)/float(annual_salary))*12*100
bill_percentage=float(monthly_bills)/float(annual_salary)*12*100
food_percentage=float(weekly_food)/float(annual_salary)*52*100
travel_percentage=float(annual_travel)/float(annual_salary)*100
extra_percentage=extra/float(annual_salary)*100
###Below code is to find max among all so we can print out correct no. of hyphens
max_value=max(int(mortgage_percentage),int(bill_percentage),int(food_percentage),int(travel_percentage),int(tax_percentage),int(extra_percentage))

print(" ")
print("------------------------------------------"+'-'*max_value)
print("See the financial breakdown below, based on a salary of $"+annual_salary)  
print("------------------------------------------"+'-'*max_value)
print("| mortgage/rent | $",format(float(monthly_mortgage)*12,'10,.2f'),"| "+str(format(mortgage_percentage,'5.1f'))+"% | "+'#'*int(mortgage_percentage))
print("|         bills | $",format(float(monthly_bills)*12,'10,.2f'),"| "+str(format(bill_percentage,'5.1f'))+"% | "+'#'*int(bill_percentage))
print("|          food | $",format(float(weekly_food)*52,'10,.2f'),"| "+str(format(food_percentage,'5.1f'))+"% | "+'#'*int(food_percentage))
print("|        travel | $",format(float(annual_travel),'10,.2f'),"| "+str(format(travel_percentage,'5.1f'))+"% | "+'#'*int(travel_percentage))
print("|           tax | $",format(float(tax),'10,.2f'),"| "+str(format(tax_percentage,'5.1f'))+"% | "+'#'*int(tax_percentage))
print("|         extra | $",format(extra,'10,.2f'),"| "+str(format(extra_percentage,'5.1f'))+"% | "+'#'*int(extra_percentage))
print("------------------------------------------"+'-'*max_value)
if tax>=75000:
    print(">>> TAX LIMIT REACHED <<<")        ###To display warning for tax limit
if extra<0:
    print(">>> WARNING: DEFICIT <<<")         ###To display warning if spending is over income
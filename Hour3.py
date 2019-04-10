"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 3: Logic in Programming
Exercise:
1.
       a) Given a number, write a snippet of code that will print
            "You have money" if the number is positive,
            "You're out" if the number is zero,
            "You seem to be in debt" if less than zero"
          Your code should have an if statement, an elif statement,
          and an else.

"""

#Hour 3: Logic in Programming
balance = float(input("Insert Money Amount: $"))
if balance > 0:
    print ("You have money")
elif balance == 0:
    print ("You're out")
else:
    print ("You seem to be in debt")

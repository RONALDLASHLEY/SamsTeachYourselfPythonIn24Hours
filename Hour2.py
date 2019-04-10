"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 2: Putting Numbers to Work in Python
Exercise:
1.
       a) Write a single line of code that will satisfy this situation:

        You're ordering some supplies from a store, and you need to 
        figure out what the total price is.
        Supplies cost: $10.00
        Discount: 30%
        Sales Tax: 5%
        Shipping: $7.50

"""
####Hour 2: Putting Numbers to Work in Python

##Total = (10 - (10 * .3)) + (10 * .05)  + (7.50)
####   (Discount Price) + (Sales Tax) + (Shipping)
##print ("Total Price: $" + str(Total))

print("Total Price: $" + str((10 - (10 * .3)) + (10 * .05)  + (7.50)))

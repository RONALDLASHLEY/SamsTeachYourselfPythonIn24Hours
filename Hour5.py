"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 5: Processing Input and Output
Exercise:
1.
       a) Ask for user input of an item, the number being purchased,
            and the cost of the item. Then prit out the total and 
            thnak the user for shopping with you. Output should
            look like this:
        Give me your name, please: [Name]
        How many widgets are you buying? [#]
        How much do they cost, per item? [#.##]
        Your total is $[#.##]
        Thanks for shopping with us today [Name] !

"""

#Hour 5: Processing Input and Output
name = str(input("Give me your name, please: "))
num = float(input("How many widgets are you buying? "))
cost_per_item = float(input("How much do they cost, per item? "))
print ("Your total is $" + str(num * cost_per_item))
print ("Thanks for shopping with us today " + name + "!")

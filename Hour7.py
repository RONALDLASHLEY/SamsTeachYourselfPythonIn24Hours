"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 7: Using Loops to Repeat Code
Exercise:
1. The waiter should be able to input a value for each seat, 
    and the script should print out the total for all the seats. 
    Keep in mind that you will get both numbers and non-number
    values form the user. If an input isn't valid, you should get
    a new value from the user.
    The output should look like:

    Welcome to the receipt program!
    Enter the value for the seat ['q' to quit]: 12
    Enter the value for the seat ['q' to quit]: 15.50
    Enter the value for the seat ['q' to quit]: 9.98
    Enter the value for the seat ['q' to quit]: 14.05
    Enter the value for the seat ['q' to quit]: q
    *******
    Total: $51.53

    Welcome to the receipt program!
    Enter the value for the seat ['q' to quit]: five
    I'm sorry, but 'five' isn't valid. Please try again.
    Enter the value for the seat ['q' to quit]: 

"""

#Hour 7: Using Loops to Repeat Code
def get_value():
    print("Welcome to the receipt program!")
    q = "q"
    tot = 0.00
    while True:
        value = input("Enter the value for the seat ['q'] to quit]: ")
        if str(value) == "q":
            value = 0.00
            print("*****\nTotal: ${}".format(tot))
            break
        elif type(value) == int or type(value)== float:
            tot+= float(value)
        else:
            print("I'm sorry, but '{}' isn't valid. Please try again.".format(value))

get_value()
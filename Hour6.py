"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham

Hour 6: Grouping Items in Lists
Exercise:
1.
       a) Allow the user to input two of their favorite toppings.
            If a topping is in a list of toppings that are in stock,
            that topping is added to a new list.
            If not, a message is printed apologizing for being out of stock
            The output should look like:

            Please give me a topping: pepperoni
            We have pepperoni
            Please give me a topping: pineapple
            Sorry we don't have pineapple
            Here are your toppings: ['pepperoni']

"""

#Hour 6: Grouping Items in Lists
instock_toppings = ["sausage", "cheese", "peppers", "pepperoni"]
your_toppings = []
for i in range(2):
    topping1 = raw_input("Please give me a topping: ")
    if topping1 in instock_toppings:
        print("We have " + str(topping1))
        your_toppings.append(topping1)
    else:
        print("Sorry we don't have " + topping1)

print("Here are your toppings: " + str(your_toppings))
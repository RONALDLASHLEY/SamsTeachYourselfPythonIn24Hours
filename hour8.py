"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham
Hour 8: Using Functions to Create Reusable Code
Exercise:
1. Write a program that gets a name from a user. If that name appears in a class list, then the program should tell the user that the student is in that class. If not, it should tell the user that there's no student by that name. There should be a function that returns True if the student is present and False if not.
The output should look like:
     Welcome to the student checker!
     Please give me the name of a student (enter 'q' to quit): student1
     No, that student is not in the class.
     Please give me the name of a student (enter 'q' to quit): student2
     Yes, that student is in the class!
     Please give me the name of a student (enter 'q' to quit): q
     Goodbye!
"""

print('Welcome to the student checker!')

students = ['student2']
in_put = ''

def student_checker(student):
    if student in students:
        print("Yes, that student is in the class!")
    elif student == 'q':
        pass
    else:
        print("No, that student is not in the class.")
        
def get_input(in_put):
    while in_put != 'q':
        in_put = raw_input("Please give me the name of a student (enter 'q' to quit): ")
        student_checker(in_put)
    else:
        print("Goodbye!")

get_input(in_put)
"""
Sams Teach Yourself Python in 24 Hours
by Katie Cunningham
Hour 9: Using Dictionaries to Pair Keys with Values
Exercise:
1. Create a program that pairs a students name to his class grade. The user should be able to enter as many students as needed and then get a printout of all the students names and grades.
The output should look like this:

    Please give me the name of the student (enter 'q' to quit): [Input]
    Please give me their grade: [Input]
    Please give me the name of the student (enter 'q' to quit): q
    Okay, printing grades!
    
    Student   Grade
    Student1    A
    Student2    D
    Student3    B
    Student4    A
    
"""

import pandas as pd

#Dictionary of student grades already entered
student_grades = {'Student1':'A', 'Student2':'D'}
student_name = ''

#Get student name from user
def get_input(student_name):
    while student_name != 'q':
        student_name = raw_input("Please give me the name of the student (enter 'q' to quit): ")
        check(student_name)
    else:
        print_grades()

#Check if student grade is already entered
#If entered, offers opportunity to change grade
def check(student_name):
    if student_name not in student_grades.keys():
        add_grade(student_name)
    else:
        print('Student: ' + student_name + '\nCurrent Grade  : ' + student_grades[student_name])
        update_query = raw_input("Would you like to update "+ student_name + " grade? ")
        if update_query == 'Yes':
            update_grade(student_name)
        else:
            pass

#Insert grade for studnets        
def add_grade(student_name):
    if student_name != 'q':
        insert_grade = raw_input("Grade: ")
        student_grades.update({student_name:insert_grade})
    else:
        pass

#Update grade for student with grade already entered
def update_grade(student_name):
    input_grade= raw_input("Change  grade to: ")
    student_grades.update({student_name:input_grade})

#Display student and grades using pandas.DataFrame
def print_grades():
    stu_names,stu_grades = (student_grades.keys()), (student_grades.values())
    df = pd.DataFrame(data={'Student': stu_names, 'Grade': stu_grades })
    display_grades = df[['Student','Grade']]
    print("Okay, printing grades!")
    print(display_grades.sort_values(by=['Student']))
    
def main():
    get_input(student_name)
    
if __name__ == '__main__':
    main()
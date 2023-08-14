"""Implement a function named get_student_data(). The function should do the following:
Using input() it asks for name, first name and a student-id.
The values are packed into a tuple.
This tuple is returned from the function
The function get_student_data() is then called in the program, the return value is 
assigned to a variable. Finally, output the variable using print()."""

name=input("Please enter a Name: ")
firstname= input("Please enter a FirstName: ")
student_id =int(input("Please enter Id: "))
student_details=(name,firstname,student_id) 
def get_student_data():      
    return student_details
for student in get_student_data():
    print(student)
    
    
    
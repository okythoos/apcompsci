import csv
from csv import writer

print ("Roybal Learning Center")
print ("Students Data")

st = True 
while st:

  # we create the variable name
  name = input ("Your Name: -q- to exit ")
  if name == "q":
    st = False
  else:
    
    print ("Hello "+ name)

    # the variable age is an integer vairable
    age = input (name + " How old are you? ")

    grade = input (name + "What grade are you in" )


    if grade = "9" or grade == "12":
      couns = "Lexius"
    elif grade == "10":
      couns = "Gonzalez"
    elif grade == "11":
      couns = "White"
    Print ("Your counselor is " +couns)
    


    couns = input ("Your conselor: ")

    # we create the variable gpa
    gpa = float (input("Enter your GPA "))

    if gpa < 1.5:
      print ("You have a low gpa:")

    elif gpa >=1.5 and gpa <2.5:
      print ("You are kinda okay")

    else: 
      print ("You have a good GPA")

print ("Roybal Learning Center")
print ("Students Data")

st = True 
while = st:

  # we create the variable name
  name = input ("Your Name: -q- to exit ")
  lf name == "q":
    st = False
  else:
    
    print ("Hello "+ name)

    # the variable age is an integer vairable
    age = input (name + " How old are you? ")

    # we create the variable gpa
    gpa = float (input("Enter your GPA "))

    if gpa < 1.5:
      print ("You have a low gpa:")

    elif gpa >=1.5 and gpa <2.5:
      print ("You are kinda okay")

    else: 
      print ("You have a good GPA")
  

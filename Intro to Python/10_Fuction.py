# A simple Python function
 
def fun():
  print("Welcome to Chilla")


  # A simple Python function
 
def fun():
  print("Welcome to Chilla")
         
# Driver code to call a function
fun()


# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
evenOdd(2)
evenOdd(3)



# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='Python', lastname='Practice')
student(lastname='Practice', firstname='Python')


print("-------- Practice With Fuction ---------")

name = str(input("Enter Your Name :"))
def student(name):

    if(name == "Ahsan" ):
      print("You Are Student Of Sukkur IBA University")
    else:
      print("You Are Not Student Of SIBA")


student(name)


print("----- Grading Exercise With Fuction ------")

marks = int(input("Enter Your Marks For Grades : "))
def grade(marks):
    if(marks>90 and marks<100):
      print("You Got A1 grade And Excellent")
    elif(marks>85 and marks<90):
      print("You Got A grade And good")
    elif(marks>75 and marks<85):
      print("You Got B grade And satisfactory")
    elif(marks>65 and marks<75):
      print("You Got C grade And passing")
    elif(marks>50 and marks<65):
      print("You Are Just Pass")
    else:
      print("Bullshit Your Are Fail In Exam")

grade(marks)


# returning the function

def convert_seconds(seconds):
   hours = seconds//3600
   minutes = (seconds - hours*3600)//60
   remaining_sec = seconds - hours*3600 - minutes*60
   return hours,minutes,remaining_sec


hours,minutes,seconds= convert_seconds(200000)
print("Remaining Time =",hours,"Hours",minutes,"Minutes",seconds,"Seconds")

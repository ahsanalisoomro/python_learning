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




name = str(input("Enter Your Name :"))
def student(name):

    if(name == "Ahsan" ):
      print("You Are Student Of Sukkur IBA University")
    else:
      print("You Are Not Student Of SIBA")


student(name)
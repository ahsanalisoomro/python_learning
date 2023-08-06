
# Python program to illustrate if-elif-else ladder
#!/usr/bin/python

i = int(input("Enter the Enter :"))
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")

print("---------New program -------------")

Age = int(input("Enter The Age Of Atif : "))

if(Age > 7 and Age <10):
    print("Atif is Child Going for Masjid.. ")
elif(Age>10 and Age<11):
    print("Atif is Eligibe for School..")
elif(Age> 11 and Age<13):
    print("Atif is now going for Primary School")
elif(Age>13 and Age<15):
    print("Atif is Going for Secondary School And Get 1st Position")
elif(Age>15 and Age<18):
    print("Atif is now Get Addmission Into High School")
elif(Age>18 and Age<20):
    print("Now Atif is Passout From HSSC Thull")
elif(Age>20 and Age<26):
    print("Atif Is Prepare For Entrance Exam For Get Addmission In College")
elif(Age>26 and Age<30):
    print("Atif Is PassOut From University And Start JOb")
elif(Age>30):
    print("Atif Is Statring Job")
else:
    print("Atif BABY Boy No Enter In School")
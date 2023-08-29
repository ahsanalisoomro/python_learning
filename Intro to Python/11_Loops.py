# Python program to illustrate
# Basic Program

languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)
  #-----------------------------
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
#----------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#--------------------------------------
for b in range(6):
  print(b)
else:
  print("Finally finished!")

#--------------------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
  for h in fruits:
    print(a, h)
#--------------------------------------
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Students")


for letter in 'geeksforgeeks':
 
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
 
print('Current Letter :', letter)


# Python program to illustrate
# Iterating over range 0 to n-1
 
n = 4
for i in range(0, n):
    print(i)

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])


for count in range(2, 30, 3):
  print(count)


# use dictionary using loops

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)


# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)



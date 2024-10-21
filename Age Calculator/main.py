from datetime import date

a = input("Enter your name : ")

b =  int(input("Enter your birth year : "))

# c= int(input("Enter the present  year : "))

c = date.today().year

b -= c

print(f'{a}  your age is : {-b}')
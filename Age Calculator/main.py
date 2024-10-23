from datetime import date

Name = input("Enter your name : ")

birth_year =  int(input("Enter your birth year : "))

# c= int(input("Enter the present  year : "))

current_year = date.today().year

birth_year -= current_year

print(f'Hello {Name}!,your age is : {-birth_year}')
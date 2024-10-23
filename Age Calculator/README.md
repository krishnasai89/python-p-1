# Required python packages
*Now that we have the packages, we are ready to import it in our python script.*
```py
from datetime import date
```
- *This imports the date class from the datetime module, which you'll use to get the current year.*
```py
Name = input("Enter your name : ")
birth_year =  int(input("Enter your birth year : "))
```
- *These lines prompt the user to enter their name and birth year. The name is stored in the variable Name, and the birth year is converted to an integer and stored in brith_year.*
```py
current_year = date.today().year
```
- This gets the current year from the system's date and stores it in the variable current_year.
```py
b -= c
```
- This line subtracts the birth year from the current year to get the age of the user.
```py
print(f'Hello {Name}!,your age is : {-birth_year}')
```
- This line prints out a greeting message with the user's name and age.

output : 
```cmd
Enter your name : John
Enter your birth year : 1990
Hello John!,your age is : 32
```

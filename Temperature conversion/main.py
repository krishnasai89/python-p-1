unit = input("Is this temperature in Celsius or Fahreheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    #((°c *9/5) +32)
    temp =round((temp * 9/5) +32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    #(°F - 32)*5/9=°C
    temp=round((temp - 32)*5/9,1)
    print(f"The temperature in Fahrenheit is: {temp}°C")

else:
    print(f"{unit} is an invalid unit of mesurement")
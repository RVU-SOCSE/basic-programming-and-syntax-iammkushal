
#prog to find temperture
#USN :1RUA25BCA0053
#Name : Kushal R



print("1.celsius to fahrenheit conversion")
print("2.fahrenheit to celsius conversion")

choice = int(input("enter your choice"))
temp = float(input("enter the temperature"))
match choice:
             case 1:
               fahrenheit = (temp * 9/5)+32
               print("the fahrenheit temperture is",fahrenheit)
             case 2:
               celsius = (temp - 32)*5/9
               print("the celsius temperature is ",celsius)
             case _:
               print("invalid")

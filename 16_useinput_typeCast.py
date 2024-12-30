a=input(" Enter the number: ")
b=input(" Enter the Number 2: ")
print(a+b)                      # this Consider input as string  and Concatinate them

print("\n Inter Type")
c=int(input(" Enter the number1: "))
d=int(input(" Enter the Number 2: "))
print(c+d)


print("\n Float Type")
c=float(input("Enete float number"))
d=float(input("enter 2nd float Number"))
print(c,d,c+d)

print("Eval Type")
c=eval(input("Enter any  1st Value: " ))             # Eval Only Takes number value to perfornm opreation
d=eval(input("Enter  any 2nd Value: " ))             # Eval also convert binary To Number   (Try: 0b1010)
print(c+d)
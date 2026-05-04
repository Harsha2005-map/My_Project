'''''
# This program checks whether the number is positive, negative or zero. 
n=int(input("Enter number:"))
if n>0:
    print("Positive number")
elif n<0:
    print("Negative Number")
else:
    print("It is Natural number")
''
number=int(input("Enter a numebr:"))
result=(
    "Positive number" if number >0
    else "Negative number" if number <0
    else "It is a natural number"
)
print(result)
'''
age=20
citizen=True
result=(
    "Citizen"
    if age >=18 and citizen
    else "Not a citizen"
)
print(result)
import random
import math

print("this will generate a random number between 1 and 10")
print(random.randint(1, 10 ))


fun_choices= ["sqrt", "ceil", "floor", "fabs", "gcd", "copysign"]

print(random.choices(fun_choices, weights = [1, 1, 1, 1, 1, 1], k = 1))

number = random.randint(1, 5)

x = 0
while x == 0:
    guess =  int(input("enter a number to guess: "))
    if number == guess:
        print("wow you got it right !")
        x = 1
        continue
    else:
        print("you got it wrong try again")
        
# i dont understand how to make the loop go again when guess doesnt equal input

x = float(input("enter a decimal number: "))
print(f"round up of number: {math.ceil(x)}")
print(f"round down of number: {math.floor(x)}")

a = -5 
b = 10
print(f"a  = {a}")
print(f"b  = {b}")
print(f"copysign: {math.copysign(b,a)}")
print(f"absolution of number: {math.fabs(a)}")
    
c = int(input("enter a number: "))
d = int(input("enter another number; "))
print(f"the greatest common divior of the two numbers are: {math.gcd(c,d)}")
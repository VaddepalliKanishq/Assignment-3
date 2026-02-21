import math

while True:
    num = input("Enter your number: ")
    if num.isdigit():
        num = int(num)
        print(f"Square root : {math.sqrt(num)}")
        print(f"Logarithm : {math.log(num)}")
        print(f"Sine : {math.sin(num)}")
        break
    else:
        print("Invalid input. Enter a positive integer.")

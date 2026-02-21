def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

while True:
    num = input("Enter your number: ")
    if num.isdigit():
        num = int(num)
        print(f"Factorial of {num} is : {fact(num)}")
        break
    else:
        print("Invalid input. Enter a positive integer.")
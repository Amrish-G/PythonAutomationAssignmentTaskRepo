#Factorial Program

number = int(input("Enter a number to find its factorial : "))
print("Given number is ",number," and its factorial is")
factorial_result = 1
while number > 1:
    print(number,"x", (number-1))
    factorial_result *= number
    number -= 1

print("Factorial for given number",number,"is",factorial_result)

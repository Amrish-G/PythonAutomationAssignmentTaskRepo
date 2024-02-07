'''
program that takes two numbers as input and
prints whether the first number is greater than, less than, or equal to the second number.
'''

first_number = float(input("Enter first number : "))
second_number = float(input("Enter second number : "))
b = first_number > second_number == True
first_condition = first_number > second_number
print("First number is greater than second number is",first_condition)
second_condition = first_number < second_number
print("First number is less than second number is",second_condition)
final_condition = first_number == second_number
print("Both first number and second number are same",final_condition)

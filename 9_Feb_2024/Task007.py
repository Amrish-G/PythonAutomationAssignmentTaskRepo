'''
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input  side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
'''

side_a = float(input("Enter length of side-A : "))
side_b = float(input("Enter length of side-B : "))
side_c = float(input("Enter length of side-C : "))

if side_a == side_b == side_c:
    print("Given length of all three sides defines that it is a Equilateral triangle")
elif (side_a == side_b) or (side_a == side_c) or (side_b == side_c):
    print("Given length of all three sides defines that it is a Isosceles triangle")
elif (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
    print("Given length of all three sides defines that it is a Scalene triangle")
else:
    print("Unable to define given triangle")
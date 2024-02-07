'''
Python program to calculate the area of a circle
given its radius using the formula area=π×r^2 ( Take pie as 3.14)
'''

PI = 3.14
radius = float(input("Enter radius of circle : "))
area_of_circle = PI*(radius**2)
print("Area of circle for given radius is ->","\n{} x {}^2 =".format(PI, radius),area_of_circle)
print(type(PI))
print(type(radius))
print(type(area_of_circle))
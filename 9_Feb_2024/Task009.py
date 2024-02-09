#Fibonnacci series

number = int(input("Enter a number : "))
a = 0
b = 1
temp = 0
print(a)
print(b)
#Invoking looping concept for getting fibonnacci series
for i in range(2,number):
    temp = (a+b)
    print(temp)
    a = b
    b = temp
print("-------------")
#Invoking while loop for getting the fibonnaci series
i = 2
c = 0
d = 1
temp_2 = 0
print(c)
print(d)
while i <= number:
    temp_2 = (c + d)
    print(temp_2)
    c = d
    d = temp_2
    i+=1
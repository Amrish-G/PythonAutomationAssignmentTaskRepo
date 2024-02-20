'''
Palindrome checker program
'''

#Checking Palindrom using while loop

word = input("Enter a word to check : ")
temp_rev_str_1 = ""
i = len(word) - 1
while i >= 0:
    temp_rev_str_1 += word[i]
    i = i - 1
print("Checking in While loop")
if (word.lower() == temp_rev_str_1.lower()):
        print("Given ", word, " is palindorme")
else:
        print("Not Palindrome")

#checking in for loop

temp_rev_str_2 = ""
for i in word:
    temp_rev_str_2 = i + temp_rev_str_2
print("Checking in For loop")
if(word.upper() == temp_rev_str_2.upper()):
    print("Given ", word, " is palindorme")
else:
    print("Not Palindrome")

#checking with in-built string function

print(reversed(word))

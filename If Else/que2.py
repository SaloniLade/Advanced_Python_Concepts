#1.Write a python program that reads a value of n and check the number is zero or non zero value
# n=int(input("enter a Number:"))
# if n==0:
#     print("Zero value")
# else:
#     print("Non zero value")


#2.Write a python program to find a largest of two Numbers 
# n=int(input("Enter the first Number:"))
# m=int(input("Enter the second Number:"))
# if n>m:
#     print(n, "is a Largset Number")
# else:
#     print(m, "is a Largest Number")


#3.Write a python program that reads the number and check the number is positive or negative
# n=int(input("Enter the Number:"))
# if n>0:
#     print(n, " is positive Number")
# else:
#     print(n, " is negative Number")


#4.Write a python program to check entered character is vowel or consonant
# char=input("Enter  a Character:")
# if char=='A'or char=='E'or char=='I'or char=='O'or char=='U'or char=='a'or char=='e'or char=='i'or char=='o'or char=='u':
#     print("vowel")
# else:
#     print("consonant")    


#5.Write a python program to evaluate student performance
# per=int(input("Enter your Percentage:"))
# if per>=90:
#     print("Excellent Performance..!!")
# elif per>=80 and per<90:
#     print("Very good Performance")
# elif per>=70 and per<80:
#     print("Good performance")
# elif per>=60 and per<70:
#     print("Average Performance")
# else:
#     print("Poor Performance")


#6.Write a python program to find largest of three Numbers
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=int(input("Enter third number:"))
# if a>b and a>c:
#     print(a,"is largest number")
# elif b>a and b>c:
#     print(b,"is largest number")
# else:
#     print(c,"is largest number")


#7.Write a python program to find smallest of three numbers
# a=int(input("Enter first Number:"))
# b=int(input("Enter second Number:"))
# c=int(input("Enter third Number:"))
# if a<b and a<c:
#     print(a," is Smallest Number")
# elif b<a and b<c:
#     print(b,"is smallest Number")
# else:
#     print(c,"is smallest Number")


#8.Write a python program to check whether number is even or odd
# n=int(input('Enter a Number:'))
# if n%2==0:
#     print(n,"is Even Number")
# else:
#     print(n,"is odd Number")


#9.Write a python program to check year for a leap year
# year=int(input("enter the Year:"))
# if (year%4==0) or (year%400==0 and year%100!=0):
#     print(year,"is leap year")
# else:
#     print(year,"is not leap year")


#10.A company insures its drivers in the following cases:
#if the driver is married.and if  the driver is unmarried ,male and above 30 years of age.
#if the driver is unmarried,female and above 25 years of age.
#In all the other  cases, the driver is not insured. Write a python program to determine whether the driver is insured or not.
# Write a Python program to determine whether the driver is insured or not

# marital_status = input("Enter marital status (married/unmarried): ")
# gender = input("Enter gender (male/female): ")
# age = int(input("Enter age: "))

# if marital_status == "married":
#     print("Driver is Insured")

# elif marital_status == "unmarried" and gender == "male" and age > 30:
#     print("Driver is Insured")

# elif marital_status == "unmarried" and gender == "female" and age > 25:
#     print("Driver is Insured")

# else:
#     print("Driver is Not Insured")
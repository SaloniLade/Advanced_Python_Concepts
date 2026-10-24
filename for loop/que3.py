#1.Write a python program to print the natural numbers up to n
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     print(i)


#2.Write a python program to print even numbers up to n
# n=int(input("Enter the value of n:"))
# for i in range(2,n+1,2):
#     print(i)


#3.Write a python program to print odd numbers up to n
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1,2):
#     print(i)


#4.Write a python program that prints 1 2 4 8 16  25 32 ....n^2
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     print(i*i)


#5.Write a python program to sum the given sequence 
#1 + 1/1! + 1/2! + 1/3! + ....  +1/n!
# n = int(input("Enter the value of n: "))
# fact = 1
# sum = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + 1 / fact
# print("Sum of the series =", sum)


# 6.Write a python program to conpute the cosine series
# cos(x) = 1 -x^2/2! + x^4/4! - x^6/6! + .......x^n /n!
# x = float(input("Enter the value of x: "))
# n = int(input("Enter the number of terms: "))
# sum = 0
# for i in range(n):
#     fact = 1
#     for j in range(1, 2*i + 1):
#         fact = fact * j
#     sum = sum + ((-1)**i * x**(2*i)) / fact
# print("Cosine series sum =", sum)


# 7. Python Program to Check Whether the Square Root of a Number Is Prime or not.
# import math
# n = int(input("Enter a number: "))
# root = int(math.sqrt(n))
# if root * root == n and root > 1:
#     prime = True
#     for i in range(2, root):
#         if root % i == 0:
#             prime = False
#             break
#     if prime:
#         print("Square root is prime")
#     else:
#         print("Square root is not prime")
# else:
#     print("Square root is not prime")



# Write a python program to produce the following design

# A  B  C
# A  B  C
# A  B  C

# n=int(input("Enter value of n: "))
# for i in range(n):
#     for j in range(3):
#         print (chr(65 + j), end=" ")
#     print()    


# A
# A  B   
# A  B  C
# A  B  C  D
# A  B  C  D  E

# n=int(input("Enter the value of n: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print (chr(65+j),end=" ")
#     print()    


# A B C D E
# A B C D
# A B C
# A B
# A

# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()



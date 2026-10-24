#1.String Length
#Write a program to input a string and display its length without using the len() function
# str=input("Enter a String:")
# count=0
# for ch in str:
#     count=count+1
# print("Length of String=",count)

#2.Character Count
#Count the number of vowels,consonants ,digits,spaces and special characters in a given string
# str=input("Enter a String:")
# vowels=0
# consonants=0
# digits=0
# spaces=0
# special=0
# for ch in str:
#     if ch in "aeiouAEIOU":
#         vowels=vowels+1
#     elif ch.isalpha():
#         consonants=consonants+1
#     elif ch.isdigit():
#         digits=digits+1
#     elif ch.isspace():
#         spaces=spaces+1
#     else:
#         special=special+1
# print("Vowels:",vowels)
# print("Consonants:",consonants)
# print("Digits:",digits)
# print("Spaces:",spaces)
# print("Special Characters:",special)

#3.Reverse a String
#Reverse the  given string without using built in reverse function
# str=input("Enter a String:")
# rev=" "
# for ch in str:
#     rev=ch+rev
# print("Reversed String:",rev)

#4.Paliandrome Check
#Check whether the entered string is paliandrome.
# str=input("Enter a String:")
# rev=""
# for ch in str:
#     rev=ch+rev
# if str==rev:
#     print("Paliandrome String")
# else:
#     print("Not paliandrome String")    

#5.Uppercase and Lowercase count
#Count the number of uppercase and lowercase letters in string
# str=input("Enter a String:")
# uppercase=0
# lowercase=0
# for ch in str:
#     if ch.isupper():
#         uppercase=uppercase+1
#     elif ch.islower():
#         lowercase=lowercase+1
# print("Uppercase letters:",uppercase)
# print("Lowercase letters:",lowercase)

#6.Replace Characters
#Replace all occurence of given character with another character
# str=input("Enter a String:")
# old=input("Enter a character you wants to replace:")
# new=input("Enter a new character:")
# result=" "
# for ch in str:
#     if ch==old:
#         result=result+new
#     else:
#         result=result+ch
# print("New String:",result)

#7.Remove Spaces
#Remove all spaces from the given string
# str=input("Enter a String:")
# result=" "
# for ch in str:
#     if ch !=" ":
#         result= result+ch
# print("String Without space:",result)

#8.Frequncy of characters
#Find the number of times a specified character appears in a string
# str=input("Enter a string:")
# ch=input("Enter a character you wants to count:")
# count=0
# for letter in str:
#     if letter==ch:
#         count=count+1
# print("Number of Occurence:",count)

#9.First and Last Character
#Print the first and last character of the string
# str=input("Enter a String:")
# print("First Character:",str[0])
# print("Last character:",str[-1])

#10.ASCII value
#Display each character of a string along with its ASCII Value
# str=input("Enter a String:")
# for ch in str:
#     print(ch, "=",ord(ch))

#11.Word count
#Count the total number of words in a sentence
# str=input("Enter a Sentence:")
# count=1
# for ch in str:
#     if ch==" ":
#         count=count+1
# print("Total number of words:",count)

#12.Longest Word
#Find a longest word in a given sentence
# sentence=input("Enter a Sentence:")
# words=sentence.split()
# longest=max(words,key=len)
# print("Longest Word:",longest)

#13.Shortest word
#Find the shortest word in a given sentence
# sentence=input("Enter a sentence:")
# words=sentence.split()
# shortest=min(words,key=len)
# print("Shortest word:",shortest)

# 14.Title case
# convert the first letter of word to uppercase
# sentence=input("Enter a Sentence:")
# print("Title case:",sentence.title())

# 15.Duplicate characters
# Print all duplicate characters in a string
# str=input("Enter a String:")
# duplicates=" "
# for ch in str:
#     if str.count(ch)>1 and ch not in duplicates:
#         duplicates=duplicates+ch
# print("Duplicate Characters :",duplicates)

#16.character frequency
#display the frequency of every chharacter in a string
# str=input("Enter a String: " )


#18.remove duplicate characters
#remove duplicate characters while maintaining original order
# s=input("Enter a String:")
# result = ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print("After removing duplicates:", result)

# 19.Substring Check
# main_string = input("Enter main string: ")
# substring = input("Enter substring: ")
# if substring in main_string:
#     print("Substring exists")
# else:
#     print("Substring does not exist")

# 20.Count Occurence of word
# sentence = input("Enter a sentence: ")
# word = input("Enter the word to count: ")
# words = sentence.split()
# count = words.count(word)
# print("Occurrences:", count)

# 21.Password Validator
# import re
# password = input("Enter password: ")
# if (len(password) >= 8 and
#     re.search("[A-Z]", password) and
#     re.search("[a-z]", password) and
#     re.search("[0-9]", password) and
#     re.search("[^A-Za-z0-9]", password)):
#     print("Valid Password")
# else:
#     print("Invalid Password")

# 22.Run length Encoding
# s = input("Enter a string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# print("Compressed string:", result)

# 23.Sring Compression
# s = input("Enter a string: ")
# result = ""
# count = 1
# for i in range(len(s)):
#     if i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#     else:
#         result += s[i] + str(count)
#         count = 1
# if len(result) < len(s):
#     print("Compressed string:", result)
# else:
#     print("Original string:", s)

# 24.Most frequent character
# s = input("Enter a string: ")
# max_count = 0
# most_frequent = ""
# for ch in s:
#     count = s.count(ch)
#     if count > max_count:
#         max_count = count
#         most_frequent = ch
# print("Most frequent character:", most_frequent)
# print("Frequency:", max_count)

# 25.Second most frequent charater
# s = input("Enter a string: ")
# frequency = {}
# for ch in s:
#     frequency[ch] = frequency.get(ch, 0) + 1
# values = sorted(set(frequency.values()), reverse=True)
# if len(values) < 2:
#     print("Second most frequent character does not exist")
# else:
#     second_frequency = values[1]
#     for ch in frequency:
#         if frequency[ch] == second_frequency:
#             print("Second most frequent character:", ch)
#             print("Frequency:", second_frequency)
#             break

# 26.Caesar  cipher
# def caesar_cipher(text, shift):
#     result = ""
#     for ch in text:
#         if ch.isalpha():
#             base = ord('A') if ch.isupper() else ord('a')
#             result += chr((ord(ch) - base + shift) % 26 + base)
#         else:
#             result += ch
#     return result

# text = input("Enter message: ")
# shift = int(input("Enter shift: "))
# encrypted = caesar_cipher(text, shift)
# decrypted = caesar_cipher(encrypted, -shift)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)

# 27.Email validator
# import re
# email = input("Enter email address: ")
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")
    
#28.word Frequency Dictionary
# paragraph = input("Enter a paragraph: ")
# words = paragraph.lower().split()
# frequency = {}
# for word in words:
#     word = word.strip(".,!?;:")
#     frequency[word] = frequency.get(word, 0) + 1
# print("Word Frequency:")
# for word, count in frequency.items():

#29.Sentence Reversal
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# words.reverse()
# result = " ".join(words)
# print("Reversed sentence:", result)

#30.String Rotation
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) == len(str2) and str2 in str1 + str1:
#     print("Yes, it is a rotation")
# else:
#     print("No, it is not a rotation")
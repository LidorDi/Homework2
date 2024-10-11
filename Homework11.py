import random as random
from tkinter.filedialog import LoadFileDialog

# assignment 1

list1: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(list1)
print(f" is all of the list true?  : {all(list1)}")
print(f" at least 1 true? : {any(list1)}")
print(f"list is only false? : {list1.count(False) == 3}")
print(f"list has at list 1 false? : {not list1.count(False) == 0}")

print()

list2: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(list2)
print(f"all numbers are diffrent than 0? : {list2.count(0) == 0}")
print(f"at list 1 number diffrent than 0? : {list2.count(0) < 5}")
print(f"all numbers are 0? : {not list2.count(0) < 5}")
print(f"atlist one 0 number? : {list2.count(0) > 0}")

print()

# assignment 2
str1 = "lidor diey, lod"
print(len(str1))
print(str1.upper())
print(str1.lower())
print(f"is the str starts with my name? : {str1.startswith("lidor") == True}")
print(f"is the str ends with my city? : {str1.endswith("lod") == True}")
print(str1.split())
str2 = str1.replace(" ", "*")
print(str2)
print(str2.split())
string1: str = "=" + str1 + "="
print(string1.center(50))
print(string1[4:])
print(string1[:4])
print(string1[2::2])
print(string1.title())

print()

# Assignment 3

string4: str = " fun-day "
print(string4.replace(" ", ""))
string5: str = "hello"
print(f"is the string only with letters? : {string5.isalpha()}")
string6: str = "777"
print(f"is it only digit ?: {string6.isdigit}")
string7: str = " "
print(f"is the string only has spaces?: {string7.isspace()}")
strlist: list[str] = ["N", "I", "N", "J", "A"]
print("".join(strlist))
strlist2: list[str] = []
for i in strlist:
    strlist2 += i + "*"
print("".join(strlist2))
string8: str = "hELLo"
string9: str = string8.lower()
print(f"does the string has e in it?: {string9.count("e") > 0}")

print()

# bonus
# לא הבנתי מה זאת אומרת comperhension אז עשיתי בעצמי. אשמח שתוכל לפרט
letter: str = str(input("enter a word"))
listp: list[str] = []
for i in letter:
    if i.isalpha():
        listp.append(i)
print(listp)
letter1:str = "".join(listp)
print(letter1.upper())


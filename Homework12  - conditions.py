# Assignment 1

number: float = float(input("input a decimal number"))
if number > 10:
    print(number - 10)
else:
    print(number * 10)

# Assignment 2

number1: float = float(input("input a decimal number"))
number2: float = float(input("input a second decimal number"))
number3: float = float(input("input a third decimal number"))
sumnumbers = number1 + number2 + number3
if sumnumbers > 100:
    print(sumnumbers)

# Assignment 3 - bonus

number4: float = float(input("enter a decimal number"))
number5: float = float(input("enter a second decimal number"))
number4i: float = number4 - int(number4)
number5i: float = number5 - int(number5)
if number4i == number5i:
    print("equal")
else:
    if number4i > number5i:
        print(number4i)
    else:
        print(number5i)

# Assignment 4

number6: int = int(input("enter ur age"))
if number6 > 120 or number6 < 0:
    print("not valid age")
else:
    print(number6)

# Assignment 5

number7: int = int(input("enter a 3 digit number"))
print((number7 % 100) // 10)

# Assignment 6

number8: int = int(input(" enter a positive number"))
for i in range (number8,0 , -1):
    print(i)

# Assignment 7

number9: int = int(input(" enter a number"))
number10: int = int(input(" enter a second  number"))
if number9 > number10:
    for i in range (number10 , number9 + 1, 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range (number9 , number10 + 1, 1):
        if i % 2 == 0:
            print(i)

# Assignment 8

number11: int = int(input("enter a number"))

for i in range(1, number11 + 1):
    if i % 5 == 0 or i % 3 == 0:
        print(i)

# Assignment 9

number12: int = int(input("enter a positive number"))
for i in range(1, number12):
    if i % 7 == 0:
        print(i)

# Assignment 11

sumnumber13 = 0
while True:
    number13: int = int(input("enter a number"))
    if number13 == 0:
        break
    else:
        if number13 < 0:
            sumnumber13 += number13
print(sumnumber13)

# Assignment 12

list1: list[int] = []
for _ in range (10):
    numeber14: int = int(input("enter a number"))
    list1.append(number14)
list1.reverse()
print(list1)

# Assignment 13

list2: list[int] = []
count1 = 0
while True:
    number15: int = int(input("enter a number"))
    if number15 == 0:
        break
    else:
        for i in range(2, number15):
            if number15 % i == 0:
                count1 += 1
    if count1 == 0:
        list2.append(number15)
print(list2)

# Assignment 14

list3: list[int] = []
for _ in range(5):
    number16: int = int(input("enter a number"))
    list3.append(number16)
sumnumber16: int = sum(list3) // 5
print (sumnumber16 , "is the average")
for i in list3:
    if i >sumnumber16:
        print(i)

# Assignment 15

y: int = int(input("enter a number"))
u: int = int(input("enter another number"))
if u > y:
    print(u / y)
else:
    print(y / u)

# Assignment 16

number18: int = int(input("enter a number"))
countnumber18 = 0
while number18 > 0:
    ahadot18 = number18 % 10
    countnumber18 += ahadot18
    number18 = number18 // 10
if countnumber18 % 3 == 0:
    print("it can be devided by 3")
else:
    print("it cannot be devided by 3")

Assignment 17 - התקשתי אז נעזרתי במישהו

str1: str = str(input("enter a word"))
length = len(str1)
half = length // 2
bool_list: list[bool] = []
location = -1
for letter in str1[:half]:
    if letter == str1[location]:
        location += -1
        bool_list.append(True)
    else:
        bool_list.append(False)

if all(bool_list):
    print("meopecet")
else:
    print("not meopechet")

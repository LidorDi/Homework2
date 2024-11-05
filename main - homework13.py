# Assignment 1

import my_func

from my_func import print_stars

print_stars()
print_stars()
print_stars()
print_stars()
print_stars()

my_func.print_stars()

help(print_stars)

# Assignment 2
# a

students: int = int(input("enter how much students"))
fullclass = students // 30
last = students % 30
if last >0:
    print(f"{fullclass} full classes and another class with {last} students")
else:
    print(f"{fullclass} full classes")

# b

while True:
    try:
        x: int = int(input("enter a number"))
    except:
        print("enter an int")
        continue
    if x >= 10 and x<= 99:
        break
ahadot = x % 10
asarot = x // 10
print(ahadot * 10 + asarot)

# c
count: int = 0
for i in range(2, 200):
    for z in range(2, i):
        if i % z == 0:
            count += 1
    if count == 0:
        print(i)
############ אשמח להסבר. ניסיתי לעשות לבד אבל לא הבנתי בדיוק
# d

y1 = 0
y2 = 0
y3 = 0
y4 = 0
while True:
    y: str = str(input("enter a b c or d"))
    if y == "x":
        break
    if y == "a":
        y1 += 1
    if y == "b":
        y2 += 1
    if y == "c":
        y3 += 1
    if y == "d":
        y4 += 1

print(f"{y1} students chose a {y2} students chose b {y3} students chose c {y4} students chose d")
if y1 > y2 and y1 > y3 and y1 > y4:
    print("most answered a")
if y2 > y1 and y2 > y3 and y2 > y4:
    print("most answered b")
if y3 > y2 and y3 > y2 and y3 > y4:
    print("most answered c")
if y4 > y2 and y4 > y3 and y3 > y4:
    print("most answered d")

if y1< y2 and y1 < y3 and y1 < y4:
    print("the least answered is a")
if y2< y1 and y2 < y3 and y2 < y4:
    print("the least answered is b")
if y3< y1 and y3 < y2 and y3 < y4:
    print("the least answered is c")
if y4< y1 and y4 < y2 and y4 < y3:
    print("the least answered is d")

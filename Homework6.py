# Assignment 1
import random

a1: str = str(input("Name 1"))
a2: str = str(input("Name 2"))
a3: str = str(input("Name 3"))
a4: str = str(input("Name 4"))
mylist = [a1, a2, a3, a4]
print(random.choice(mylist))

# Assignment 2

a = random.randint(0, 100)
b: int = 200
tries = 0
while b != a:
    tries += 1
    b: int = int(input("Guess the number from 0 - 100"))
    if (b > a):
        print("your number is too big")
    elif (b < a):
        print("your number is too small")
print("bingo")

# Assignment 2.5

equal: int = 0
for i in range(0, 5, 1):
    temp: int = int(input("enter temperature"))
    while temp < -55 or temp > 45:
        temp = int(input("enter accepted temprature"))
    equal = equal + temp
last: int = equal // 5
print(last)

# Assignment 3

a: int = int(input("input a number bigger than 0"))
for i in range(a + 1):
    for i in range(1, i + 1):
        print(i, end="")
    print()
for i in range(a, 0, -1):
    for i in range(1, i):
        print(i, end="")
    print()

# Assignement 4

stars: int = int(input("input a number bigger than 0"))
minstar: int = 1
while stars >= minstar:
    print(f"{("*" * minstar):^{stars}}")
    minstar += 2

# Assignment 5 bonus tirgul

a: int = 0
b: int = a % 7
sum: int = 0
while b == 0:
    a: int = int(input("Enter a number"))
    b: int = a % 7
    if a % 11 == 0:
        break
    elif b == 0:
        sum += 1
    else:
        print(sum)

# Assignment 6 bonus tirgul

a: int = int(input("Enter a number"))
if a % 5 == 0 and a % 3 == 0:
    print("fizz buzz")
elif a % 5 == 0:
    print("fizz")
elif a % 3 == 0:
    print("buzz")

# Assignment 1
from random import random

mylist1: list[int] = [i for i in range(95, 106)]
mylist2: list[int] = [i for i in range(20, 10, -2)]
mylist3: list[str] = [random.getrandbits(1) for _ in range(5)]
mylist4: list[int] = [random.randint(1, 100) for _ in range(10)]
mylist5: list[int] = [numbers for numbers in mylist4 if numbers > 50]
mylist6: list[int] = [random.randint(1, 100) for _ in range(10)]
print(mylist6)
mylist7: list[int] = [i % 10 for i in mylist6]

# Assignment 2

# a. הם בודקים אם יש טעות ואם יש הם פועלים לפי הגדרות שהצבתי במקום להקריס את התוכנה
# b. גם כדי למצוא את הטעות וגם כדי למנוע קריסה של תוכנה במידה ויש אפשרות לטעויות בקוד

try:
    88 / 0

except:
    pass

try:
    88 / 0
    raise ZeroDivisionError
except ZeroDivisionError:
    print("cant devide by zero")

mylist8: list[int] = [1, 2, 3, 4]
while True:
    try:
        i: int = int(input("enter a number"))
        mylist8[i] = i
        if i == -999:
            break
    except IndexError:
        print("range from 0 - 3")
    except ValueError:
        print("not acceptable value")



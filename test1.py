# Test1
# תנאים

# 1

num1: float = float(input("enter a esroni number"))
num2: float = float(input("enter another esroni number"))

if num1 > num2:
    for _ in range(3):
        print(num2)
else:
    for _ in range(3):
        print(num1)

# 2

num3: int = int(input("enter a number"))
num4: int = int(input("enter another number"))
print((num3 + num4) / 2)

# 3

list1: list[int] = []
for _ in range(3):
    num5: int = int(input("enter a number"))
    list1.append(num5)
print(max(list1))

# 4

num6: int = int(input("how much minutes was the movie?"))
num7: int = num6 % 60
num8: int = num6 // 60

if num7 > 0 and num8 > 0:
    print(f"{num8} hours and {num7} minutes")
elif num7 > 0:
    print(f"{num7} minutes")
else:
    print(f"{num8} hours")

# 5 + # 6 TWO QUESTIONS IN THE SAME ANSWER

num9: int = int(input("enter a 4 digit number"))
print(f"The most right number is {num9 % 10}")
print(f"the second right number is {num9 // 10 % 10}")

# 7

num10: int = int(input("enter a 2 digit number"))
print(num10 % 10 + num10 // 10)

# 8

num11: int = int(input("enter a 2 digit number"))
print(num11 // 10 + num11 % 10 * 10)

# 9

num12: int = int(input("enter a number"))
if num12 % 2 == 0:
    print("even")
else:
    print("odd")

# 10

tax: int = int(input("how much did u make this month?"))
tax: int = 6000
if tax - 6000 <= 0:
    print(tax)
if tax - 12000 <= 0:
    print(6000 + (tax - 6000) * 0.9)
if tax - 18000 <= 0:
    print(6000 + 6000 * 0.9 + (tax - 12000) * 0.8)
if tax - 25000 >= 0:
    print(6000 + 6000 * 0.9 + 6000 * 0.8 + (tax - 18000) * 0.7)
if tax - 35000 >= 0:
    print(6000 + 6000 * 0.9 + 6000 * 0.8 + 7000 * 0.7 + (tax - 25000) * 0.6)
if tax - 50000 >= 0:
    print(6000 + 6000 * 0.9 + 6000 * 0.8 + 7000 * 0.7 + 10000 * 0.6 + (tax - 35000) * 0.55)
if tax > 50000:
    print(6000 + 6000 * 0.9 + 6000 * 0.8 + 7000 * 0.7 + 10000 * 0.6 + 15000 * 0.55 + (tax - 50000) * 0.49)

# 11

while True:
    numage: int = int(input("enter ur age"))
    numheight: int = int(input("enter ur height in cm"))
    if numheight > 115 and numage >= 8:
        print(" can go up on the train")
    elif numheight > 100 and numage >= 18:
        print(" can go up on the train ")
    else:
        print(" cant ride the train ")

# LOOPS

# 1

num13: int = int(input("enter a number"))
for i in range(1, num13):
    print(i)

# 2

num14: int = int(input("enter a number"))
num15: int = int(input("enter a number"))
if num14 > num15:
    for i in range(num15 + 1, num14):
        print(i)
else:
    for i in range(num14 + 1, num15):
        print(i)

# 3

num16: int = int(input("enter a number"))
for i in range(1, num16 + 1):
    if i % 2 == 0:
        print(f"{i}", end=" ")

# 4

nummax: int = int(input("enter a max"))
numden: int = int(input("enter a den"))
for i in range(1, nummax + 1):
    if i % numden == 0:
        print(i)

# IBOD NETONIM

# 1

list2: list[int] = []
counter1: int = 0
while True:
    num17: int = int(input("enter a number"))
    if num17 == -99 and counter1 == 0:
        print("None")
        break
    if num17 == -99:
        break
    list2.append(num17)
    counter1 += 1
print(sum(list2))

# 2

list3: list[int] = []
counter2: int = 0
while True:
    num18: int = int(input("enter a number"))
    if num18 == -99 and counter2 == 0:
        print("None")
        break
    if num18 <= 0:
        break
    counter2 += 1
    list3.append(num18)
try:
    print(f"{min(list3)} , {max(list3)}")
except:
    pass

# 3

counter3: int = 0
list4: list[int] = []
for i in range(5):
    num19: int = int(input("enter a number"))
    list4.append(num19)
print(f"the biggest number is {max(list4)} in index {list4.index(max(list4)) + 1}")

# 4

num20: int = int(input("enter a number"))
num21: int = int(input("enter another number"))
num22: int = 0
for i in range(num20):
    num22 += num21
print(num22)

# 5

num23: int = int(input("enter a number "))
num24: int = int(input("enter his hezka"))
num25: int = num23
for i in range(1, num24):
    num25 *= num23
print(num25)

# 6

num26: int = int(input("enter a number"))
num27: int = int(input("enter 1 digit number"))
while True:
    if num27 == num26 % 10:
        print("True")
        break
    if num26 == 0:
        print("False")
        break
    num26 = num26 // 10

# 7

num28: int = int(input("enter a number"))
num29: int = int(input("enter a number"))
num30: int = 0
for i in range(1, num28 + 1):
    if num28 % i == 0 and num29 % i == 0:
        num30 = i
print(num30)

# 8

num31: int = int(input("enter a number"))
counter4: int = 0
for i in range(2, num31):
    if num31 % i == 0:
        counter4 += 1
if counter4 > 0:
    print(" not a prime number ")
else:
    print("prime number")

# HARDCORE LOOPS
# לולאות מורכבות

# 1

counter5: int = 0
for i in range(12):
    num32: int = int(input("enter the temprature"))
    if num32 < -5 or num32 > 40:
        counter5 += 1
        print("wrong data")
        break
if counter5 == 0:
    print("correct data")

# 2

listbead: list[int] = []
listneged: list[int] = []
listnimna: list[int] = []
countercode: int = 0
for i in range(1, 45):
    print("pleasure")
    while True:
        try:
            numazba: int = int(input("enter ur choice"))
            if numazba < 1 or numazba > 4:
                print("choose a difrrent number")
            if numazba == 4:
                countercode += 1
                break
            else:
                break
        except:
            print("invalid syntax")
    if countercode > 0:
        print(f" country number {i} choose veto")
        break
    if numazba == 1:
        listbead.append(numazba)
    elif numazba == 2:
        listneged.append(numazba)
    elif numazba == 3:
        listnimna.append(numazba)
if countercode == 0:
    print(
        f"{len(listbead)} countrys are bead {len(listneged)} countrys are neged {len(listnimna)} countrys are nimnaim")

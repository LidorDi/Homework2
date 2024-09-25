# Assignment 1

pos = 0
neg = 0
sum7 = 0
zero = 0
lastpos = 0
lastneg = 0
for _ in range(10):
    a: int = int(input('input a number'))
    if a == -9999:
        break
    elif -1000 > a > 1000:
        continue
    elif a > 0:
        pos += 1
        lastpos: int = a
    elif a < 0:
        neg += 1
        lastneg: int = a
    elif a == 0:
        zero += 1
    if a % 7 == 0:
        sum7 += 1
if a == -9999:
    print()
elif lastpos == 0 and lastneg == 0:
    print(
        f"{pos} positive numbers, {neg} negative numbers, {zero} zero numbers, {sum7} numbers that go with 7, NONE last positive number , NONE last negative number")
elif lastpos == 0:
    print(
        f"{pos} positive numbers, {neg} negative numbers, {zero} zero numbers, {sum7} numbers that go with 7, NONE last positive number , {lastneg} last negative number")
elif lastneg == 0:
    print(
        f"{pos} positive numbers, {neg} negative numbers, {zero} zero numbers, {sum7} numbers that go with 7, {lastpos} last positive number , NONE last negative number")
else:
    print(
        f"{pos} positive numbers, {neg} negative numbers, {zero} zero numbers, {sum7} numbers that go with 7, {lastpos} last positive number , {lastneg} last negative number")

# # Assignment 2

worldrecord = None
sumscore = 0
goodscore = 0
bestscore = 0
for _ in range(7):
    a: float = float(input("enter the score in meters"))
    if 6.23 > a > 5.8:
        goodscore += 1
        sumscore = a + sumscore
    elif a > 6.23:
        worldrecord: str = str(input("name of the new world record athlete"))
        goodscore += 1
        sumscore = a + sumscore
    elif a < 5.8:
        continue
    if bestscore < a:
        bestscore = a
if worldrecord:
    print(
        f"{goodscore} good scores which {bestscore} where the best and their sum was {sumscore / 7} and the new world record older is {worldrecord} with {bestscore}")
else:
    print(
        f"{goodscore} good scores which {bestscore} where the best and their sum was {sumscore // 7} and the best score is {bestscore}")

# Assignment 3 tirgul reshot

num: int = int(input("Enter number :"))
center_position: int = int((num / 2) + 1)
space: int = center_position
for x in range(1, num + 1, 2):
    print()
    space -= 1
    print(" " * space, end="")
    for y in range(1, x + 1):
        print(f"{y}", end="")
for x in range(num - 2, 0, -2):
    print()
    space += 1
    print(" " * space, end="")
    for y in range(1, x + 1):
        print(f"{y}",end="")

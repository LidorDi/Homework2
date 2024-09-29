# Assignment 1

templist: list[float] = []
while True:
    a: float = float(input("input temp measure"))
    if a == -999:
        break
    if a < 50 and a > -50:
        templist.append(a)
tempplus = [-20.0, 39.1, 18.5]
templist.extend(tempplus)
# extend method is making a change to the list and + method is only printing the outcome but not making any change
print(f"max temp {max(templist)} min temp {min(templist)}")
print(18.5 in templist)
print(templist.count(-20))
print(sum(templist) / len(templist))
for h in templist:
    print(h, end=" ")
print()
print(templist.index(39.1))
del templist[0]
del templist[0:: 2]
templist.remove(18.5)  # if i wont check before removing it will give me a error if there isnt any
temp_last = templist.pop(len(templist))
tempnew1: list[float] = templist.copy()
tempnew1.sort()
tempnew2: list[float] = templist.copy()
tempnew2.sort(reverse=True)

# asssigment 2

mylist: list[int] = []
while True:
    print()
    a: int = int(input("enter a number"))
    if a == -999:
        break
    if a < 10 and a > 0:
        mylist.append(a)
        print("statistics", end=" ")
        for i in range(10):
            if i in mylist:
                print(f"[{i}] : {mylist.count(i)}", end=" ")

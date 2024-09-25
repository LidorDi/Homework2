# Assignent 1

mylist: list[int] = []

for i in range(1, 101):
    mylist.append(i)

print(mylist[0])
print(mylist[-1])
print(len(mylist))
print(mylist[2:12])
print(mylist[79:])
print(mylist[:17])
print(mylist[100::-1])
print(mylist[1:100:2])
print(mylist[2::3])
print(mylist[6::7])
print(mylist[9::10])
print(mylist[98:63:-3])
mylist.insert(50, 999)
mylist.pop(100)

# Assignment 2

nbalist: list[float] = []
stopper: float = 0
while True:
    stopper: float = float(input("enter their height"))
    if stopper == -999:
        break
    if stopper < 1.6 or stopper > 3:
        continue
    else:
        nbalist.append(stopper)
if len(nbalist) > 0:
    print("how much players", len(nbalist))
    print("higehst player high", max(nbalist))
    print("lowest high", min(nbalist))
    print("sum of player high", sum(nbalist) / len(nbalist))
    much: int = 0
    muchsum: int = 0
    for i in range(0, len(nbalist)):
        if nbalist[i] > 2:
            much += 1
        if (sum(nbalist)/len(nbalist)) < nbalist[i]:
            muchsum += 1
print("more than 2 meters", much)
print("more than avrage", muchsum)
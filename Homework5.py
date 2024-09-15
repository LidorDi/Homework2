# Assignment 1

time: int = int(input(" How much long the movie? type in minutes "))
hours: int = int(time // 60)
lastminutes: int = int(time % 60)
if hours > 0 < lastminutes:
    print(f"{hours} hours and {lastminutes} minutes")
elif hours > 0:
    print(f"{hours} hours")
else:
    print(f"{lastminutes} minutes")

# Assignment 2

x: int = 0
for _ in range(11):
    print(x , end=" ")
    x+=1

####################################################

for y in range(40, 89 ,2):
    print(y , end=" ")

####################################################

for y in range(77, 106, 1):
    if (y % 7) == 0:
        print(y // 7 , end=" ")

####################################################

for y in range (99, 65 , -1):
    if (y % 3) == 0:
        print(y//3 , end=" ")

# Assignment 3

x: int = 0
while x < 0.4 or x > 2.5:
    x: float = float(input("Enter your height"))
    if x < 0.4 or x > 2.5:
        print("Wrong input")

######################################################

x: int = int(input("input a number"))
y: int = int(input("input another number"))
if x > y:
    for y in range(y,x+1,1):
        print(y)
else:
    for x in range(x, y + 1, 1):
        print(x)

#######################################################

y: float = float(input("What pie is?"))
counter: int = 0
if y != 3.14:
    for _ in range(1, 3, 1):
        counter +=1
        x: float = float(input("What pie is?"))
        if x == 3.14:
            print("you are correct")
            break
        elif counter ==2:
            print("pie is 3.14")
else:
    print("you are correct")

########################################################

x: int = int(input("input a number"))
z: int = int(input("input a second number"))
y: int = int(input("input a third number"))

while  x > 10 or x < 0 or 10 > z or z > 60 or 60 > y or y > 100 or z != (y + z + x) // 3:
    x: int = int(input("input a number"))
    z: int = int(input("input a second number"))
    y: int = int(input("input a third number"))
print("DONE")

#######################################################

## ETGAR ##

beerleft: int = 10
while beerleft > 0:
    age: int = int(input("Enter your age"))
    if age >=18:
        beerleft-=1
    print(f"{beerleft} beer are left")
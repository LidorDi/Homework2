#1
from hw1_main import counter

for i in range (12, 25):
    print(i)

#2

for i in range (7,32):
    if i % 2 != 0:
        print(i)

#3

for i in range (10 , -21 , -1):
    if i % 2 == 0:
        print(i)

#4

for i in range (1, 46):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} fizzbuzz")
    elif i % 3 == 0:
        print(f"{i} fizz")
    elif i % 5 == 0:
        print(f"{i} BUZZ")

#5

list5: list = []
while True:
    x: int = int(input("enter a number, to exit enter -999"))
    if x == -999:
        break
    list5.append(x)

counter5 = 0
for i in list5:
    counter5 += i
print(counter5)

#6

def removepeople(dict6, key):
    for i in dict6:
        if key in i:
            del i[key]

def printall(dict6):
    counterfirst = 1
    counterlast = 0
    for i in dict6:
        counterfirst += 1
        if counterfirst > counterlast:
            print("")
        for b, v in i.items():
            print(f"{b} : {v} ", end=" ")
    counterlast += 1

def sortage(dict6):
    return sorted(dict6 , key = lambda i: i["age"])

list6: list[dict] =[
    {"id": 1 , "name": "Yacob" , "age": 30 , "city": "Los Santos"},
    {"id": 2 , "name": "Juli" , "age": 36 , "city": "New York"},
    {"id": 3 , "name": "Itzhak" , "age": 42 , "city": "Las Vegas"},
    {"id": 4 , "name": "Alice" , "age": 15 , "city": "Bucharest"},
    {"id": 5 , "name": "Lidor" , "age": 22 , "city": "Budsapest"}
]

#7

def printcatonly(dict7):
    for i in dict7:
        if i["animal_type"] == "cat":
            print(f"animaltype: {i["animal_type"]}")

def printanimaltype(dict7):
    counter7 = 0

    while counter7 == 0:
        x: str = str(input("enter a animal type"))
        for i in dict7:
            if i["animal_type"] == x.lower():
                print(i["names"])
                counter7 += 1
        if counter7 == 0:
            print("invalid animal type")

def add_animaltype(dict7):
    for i in dict7:
        x: str = str(input(f"enter a new {i["animal_type"]} name "))
        if x not in i["names"]:
            i["names"].append(x)

our_pets = [
{
"animal_type": "cat",
"names": [
"Meowzer",
"Fluffy",
"Kit-Cat"
]
},
{
"animal_type": "dog",
"names": [
"Spot",
"Bowser",
"Frankie"
]
}
]

#8

def printallstudent(dict8):
    for i in dict8:
        print(f"{i}: {dict8[i]}")

def add_new_hobby(dict8):
    x: str = str(input("enter a new hobby"))
    if x not in dict8["hobbies"]:
        dict8["hobbies"].append(x)

def remove_hobby(dict8):
    x:str = str(input("enter a students hobby"))
    if x in dict8["hobbies"]:
        dict8["hobbies"].remove(x)

student = {
'name': 'John',
'age': 20,
'hobbies': ['reading', 'games', 'coding'],}

add_new_hobby(student)
printallstudent(student)
remove_hobby(student)
printallstudent(student)

student.update({"family_name" : input("enter a family name")})

#9

def matrix_print(dict9):
    for i in dict9:
        for v in i:
            print(v , end=" ")
matrix =[
[1, 2],
[3, 4],
[5, 6]
]
matrix_print(matrix)

# 10

def zero_count(list):
    counter = 0
    for i in list:
        for v in i:
            if v == 0:
                counter += 1
    return counter

matrix2 =[
[0,1,1],
[0,1,0],
[1,0,0]
]
print(zero_count(matrix2))

#11

def find_dup(list):
    list1: list = []
    for i in list:
        if list.count(i) > 1:
            if i not in list1:
                list1.append(i)
    return list1

arr = [4, 2, 34, 4, 1, 12, 1, 4]
print(find_dup(arr))

#12

def reversearr(list):
    list11: list = []
    for i in range (len(list) - 1, -1 , -1):
        list11.append(list[i])
    return list11

list12 = [43, "what", 9, True, "cannot", False, "be", 3, True]
print(reversearr(list12))

#13

def arrysum(list, list2):
    list13: list = []
    for i in range (0 , len(list)):
        list13.append(list[i] + list2[i])
    return list13

#14

def palindromes(string):
    if string == string[::-1]:
        return True
    else:
        return False
first_str = "racecar"
second_str = "Java"

#15

counter15 = 1
while counter15 < 100:
    counter15 *= 2

#16

counter16 = 900000
while counter16 > 50:
    counter16 /= 2

#17 + #18 the answer is good for both

def multarray(list):
    list1: list = []
    counter = 0
    while counter < len(list):
        if list[counter] not in list1:
            list1.append(list[counter])
        counter += 1
    return list1

#19

def multarray2(list):
    list1: list = []
    counter = 0
    while counter < len(list):
        if list[counter] not in list1 and list[counter] != "pete":
            list1.append(list[counter])
        counter += 1
    return list1

#20

def boolindex(list):
    counter1 = 0
    counter = 1
    while len(list) > counter:
        if list[counter] == list[counter - 1]:
            counter1 = counter
            break
        counter += 1
    if counter1 != 0:
        return  counter1
    else:
        return -1

#21

def validationprogram():
    counter = 0
    name: str = str(input("Enter ur full name"))
    name2: str = str(input("enter again ur full name"))
    while (name.lower()).split() != (name2.lower()).split():
        name2: str = str(input("not the same full name enter again"))
    age: int = int(input("enter ur age"))
    while 1 < age > 130:
        age: int = int(input("not valid age enter again"))
    email: str = str(input("enter ur email"))
    while email.count("@") != 1:
        email: str = str(input("email not valid enter again"))


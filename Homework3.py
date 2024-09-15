# First Assignment

id: int = int(input("Enter your id"))
name: str = str(input('Enter your name'))
lastname: str = str(input('Enter your last name'))
height: float = float(input("Enter your height"))
yearofbirth: int = int(input("Enter your year of birth"))

id2: int = int(input("Enter your id"))
name2: str = str(input('Enter your name'))
lastname2: str = str(input('Enter your last name'))
height2: float = float(input("Enter your height"))
yearofbirth2: int = int(input("Enter your year of birth"))

id3: int = int(input("Enter your id"))
name3: str = str(input('Enter your name'))
lastname3: str = str(input('Enter your last name'))
height3: float = float(input("Enter your height"))
yearofbirth3: int = int(input("Enter your year of birth"))

print(f" Id: {id} Full name: {name:<10} {lastname:<10}, Height: {height:<10}, Year of birth: {yearofbirth:<10}")
print(f" Id: {id2} Full name: {name2:<10} {lastname2:<10}, Height: {height2:<10}, Year of birth: {yearofbirth2:<10}")
print(f" Id: {id3} Full name: {name3:<10} {lastname3:<10}, Height: {height3:<10}, Year of birth: {yearofbirth3:<10}")

# Second Assignment

grade: int = int(input("Enter your grade"))
if 0 >= grade <= 40:
    print("try harder next time")
elif 41 <= grade <= 60:
    print("youre getting there, need some more work")
elif 61 <= grade <= 80:
    print("pretty good")
elif 81 <= grade <= 95:
    print("awesome")
elif 96 <= grade <= 100:
    print("excellent!!! youre a star")
else:
    print("illegal grade")

# Third Assignment

vol: int = int(input("Enter volume"))
match vol:
    case 0:
        print("mute")
    case 1 | 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")

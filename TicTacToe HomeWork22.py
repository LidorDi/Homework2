import random

list2: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1: list = [0, "-", "-", "-", "-", "-", "-", "-", "-", "-"]
win = 0
tie = 0


def checkforwin(list):
    if list[1] == list[2] == list[3] != "-":
        print(f"{list[1]} won the game with a row in the first row")
        win = 1
        return win

    if list[4] == list[5] == list[6] != "-":
        print(f"{list[4]} won the game with a row in the second row")
        win = 1
        return win
    if list[7] == list[8] == list[9] != "-":
        print(f"{list[7]} won the game with a row in the second row")
        win = 1
        return win

    if list[1] == list[4] == list[7] != "-":
        print(f"{list[1]} won the game with a column in the first column")
        win = 1
        return win
    if list[2] == list[5] == list[8] != "-":
        print(f"{list[2]} won the game with a column in the second column")
        win = 1
        return win
    if list[3] == list[6] == list[9] != "-":
        print(f"{list[3]} won the game with a column in the third column")
        win = 1
        return win

    if list[7] == list[5] == list[3] != "-":
        print(f"{list[7]} won the game with a Diagonal to the right")
        win = 1
        return win
    if list[1] == list[5] == list[9] != "-":
        print(f"{list[1]} won the game with a Diagonal to the left")
        win = 1
        return win


def check_for_a_tie(list):
    counter = 0
    for i in list1:
        if i == "-":
            counter += 1
    if counter > 0:
        pass
    else:
        if list[1] == list[2] == list[3] or list[4] == list[5] == list[6] or list[7] == list[8] == list[9] or list[1] == \
                list[4] == list[7] or list[2] == list[5] == list[8] or list[3] == list[6] == list[9] or list[7] == list[
            5] == list[3] or list[1] == list[5] == list[9]:
            pass
        else:
            print("ITS A TIE")
            tie = 1
            return tie


def playervspc(list1, list2):
    counterchoose = 0
    startingplayer = 0
    list3: list = []
    print("Enter a pattern:")
    print("1. X")
    print("2. O")
    while True:
        try:
            pattern: int = int(input(""))
            if pattern != 1 and pattern != 2:
                counterchoose += 1
                if counterchoose == 5:
                    pattern: int = random.randint(1, 2)
                    AUTO = input(f"THE GAME CHOOSE ATOMATICALLY {pattern} FOR YOU, PRESS ENTER TO COUNTINUE")
                    break
                print("Not a valid number, Choose again")
                continue
        except ValueError:
            counterchoose += 1
            if counterchoose == 5:
                pattern: int = random.randint(1, 2)
                AUTO = input(f"THE GAME CHOOSE ATOMATICALLY {pattern} FOR YOU, PRESS ENTER TO COUNTINUE")
                break
            print("Not a valid Value, Choose again")
            continue
        break
    print("Who would u like to start:")
    print("1. PC")
    print("2. You")
    while startingplayer != 1 and startingplayer != 2:
        try:
            startingplayer: int = int(input(""))
            if startingplayer != 1 or startingplayer != 2:
                print("Not a valid number, Choose again")
                continue
        except ValueError:
            print("Not a valid value, Choose again")
            continue
    if pattern == 1:
        playerpattern = "X"
        pcpattern = "O"
    else:
        playerpattern = "O"
        pcpattern = "X"

    print("")
    print("")
    print("")
    print("")
    print("")
    print("TO UNDERSTAND THE BOARD PLACES HERE IS A EXAMPLE ( NUMBERS WILL BE CHANGED TO (-) AFTERWARD ")
    print(f"             I            I             ")
    print(f"      {list2[1]}      I     {list2[2]}      I      {list2[3]} ")
    print(f"             I            I             ")
    print(f"----------------------------------------")
    print(f"             I            I             ")
    print(f"      {list2[4]}      I     {list2[5]}      I      {list2[6]} ")
    print(f"             I            I             ")
    print(f"----------------------------------------")
    print(f"             I            I             ")
    print(f"      {list2[7]}      I     {list2[8]}      I      {list2[9]} ")
    print(f"             I            I             ")
    a = input("IF YOU HAVE UNDERSTOOD THE PLACES PLEASE PRESS ENTER")
    print("")
    print("")
    print("")
    print("")
    print("")

    if startingplayer == 2:
        while True:
            while True:
                print(f"             I            I             ")
                print(f"      {list1[1]}      I     {list1[2]}      I      {list1[3]} ")
                print(f"             I            I             ")
                print(f"----------------------------------------")
                print(f"             I            I             ")
                print(f"      {list1[4]}      I     {list1[5]}      I      {list1[6]} ")
                print(f"             I            I             ")
                print(f"----------------------------------------")
                print(f"             I            I             ")
                print(f"      {list1[7]}      I     {list1[8]}      I      {list1[9]} ")
                print(f"             I            I             ")
                print("")
                print(f"{playerpattern} Enter ur place ")
                while True:
                    try:
                        placechoose: int = int(input(""))
                        if placechoose < 1 or placechoose > 9:
                            print("Please choose ur place from 1 to 9 like on the board")
                            continue
                        if list1[placechoose] != "-":
                            print("Occupied already, Choose again")
                            continue
                    except ValueError:
                        print("Not a valid value, choose 1 to 9 like on the board")
                    break
                list1[placechoose] = playerpattern
                break
            if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
                break

            list3 = [i for i, x in enumerate(list1) if x == "-"]
            pcchoose = random.choice(list3)
            list1[pcchoose] = pcpattern
            if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
                break

    else:
        while True:
            list3 = [i for i, x in enumerate(list1) if x == "-"]
            pcchoose = random.choice(list3)
            list1[pcchoose] = pcpattern
            if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
                break
            while True:
                print(f"             I            I             ")
                print(f"      {list1[1]}      I     {list1[2]}      I      {list1[3]} ")
                print(f"             I            I             ")
                print(f"----------------------------------------")
                print(f"             I            I             ")
                print(f"      {list1[4]}      I     {list1[5]}      I      {list1[6]} ")
                print(f"             I            I             ")
                print(f"----------------------------------------")
                print(f"             I            I             ")
                print(f"      {list1[7]}      I     {list1[8]}      I      {list1[9]} ")
                print(f"             I            I             ")
                print("")
                print(f"{playerpattern} Enter ur place ")
                while True:
                    try:
                        placechoose: int = int(input(""))
                        if placechoose < 1 or placechoose > 9:
                            print("Please choose ur place from 1 to 9 like on the board")
                            continue
                        if list1[placechoose] != "-":
                            print("Occupied already, Choose again")
                            continue
                    except ValueError:
                        print("Not a valid value, choose 1 to 9 like on the board")
                    break
                list1[placechoose] = playerpattern
                break
            if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
                break


def playervsplayer(list1 , list2):
    counterchoose = 0
    print("The first chosen pattern starts.")
    print("Enter a pattern:")
    print("1. X")
    print("2. O")
    while True:
        try:
            pattern: int = int(input(""))
            if pattern != 1 and pattern != 2:
                counterchoose += 1
                if counterchoose == 5:
                    pattern: int = random.randint(1, 2)
                    AUTO = input(f"THE GAME CHOOSE ATOMATICALLY {pattern} FOR YOU, PRESS ENTER TO COUNTINUE")
                    break
                print("Not a valid number, Choose again")
                continue
        except ValueError:
            counterchoose += 1
            if counterchoose == 5:
                pattern: int = random.randint(1, 2)
                AUTO = input(f"THE GAME CHOOSE ATOMATICALLY {pattern} FOR YOU, PRESS ENTER TO COUNTINUE")
                break
            print("Not a valid Value, Choose again")
            continue
        break
    if pattern == 1:
        startingpattern = "X"
        endingpattern = "O"
    else:
        startingpattern = "O"
        endingpattern = "X"

    print("")
    print("")
    print("")
    print("")
    print("")
    print("TO UNDERSTAND THE BOARD PLACES HERE IS A EXAMPLE ( NUMBERS WILL BE CHANGED TO (-) AFTERWARD ")
    print(f"             I            I             ")
    print(f"      {list2[1]}      I     {list2[2]}      I      {list2[3]} ")
    print(f"             I            I             ")
    print(f"----------------------------------------")
    print(f"             I            I             ")
    print(f"      {list2[4]}      I     {list2[5]}      I      {list2[6]} ")
    print(f"             I            I             ")
    print(f"----------------------------------------")
    print(f"             I            I             ")
    print(f"      {list2[7]}      I     {list2[8]}      I      {list2[9]} ")
    print(f"             I            I             ")
    a = input("IF YOU HAVE UNDERSTOOD THE PLACES PLEASE PRESS ENTER")
    print("")
    print("")
    print("")
    print("")
    print("")
    while True:
        while True:
            print(f"             I            I             ")
            print(f"      {list1[1]}      I     {list1[2]}      I      {list1[3]} ")
            print(f"             I            I             ")
            print(f"----------------------------------------")
            print(f"             I            I             ")
            print(f"      {list1[4]}      I     {list1[5]}      I      {list1[6]} ")
            print(f"             I            I             ")
            print(f"----------------------------------------")
            print(f"             I            I             ")
            print(f"      {list1[7]}      I     {list1[8]}      I      {list1[9]} ")
            print(f"             I            I             ")
            print("")
            print(f"{startingpattern} Enter ur place ")
            while True:
                try:
                    placechoose: int = int(input(""))
                    if placechoose < 1 or placechoose > 9:
                        print("Please choose ur place from 1 to 9 like on the board")
                        continue
                    if list1[placechoose] != "-":
                        print("Occupied already, Choose again")
                        continue
                except ValueError:
                    print("Not a valid value, choose 1 to 9 like on the board")
                break
            list1[placechoose] = startingpattern
            break
        if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
            break

        while True:
            print(f"             I            I             ")
            print(f"      {list1[1]}      I     {list1[2]}      I      {list1[3]} ")
            print(f"             I            I             ")
            print(f"----------------------------------------")
            print(f"             I            I             ")
            print(f"      {list1[4]}      I     {list1[5]}      I      {list1[6]} ")
            print(f"             I            I             ")
            print(f"----------------------------------------")
            print(f"             I            I             ")
            print(f"      {list1[7]}      I     {list1[8]}      I      {list1[9]} ")
            print(f"             I            I             ")
            print("")
            print(f"{endingpattern} Enter ur place ")
            while True:
                try:
                    placechoose: int = int(input(""))
                    if placechoose < 1 or placechoose > 9:
                        print("Please choose ur place from 1 to 9 like on the board")
                        continue
                    if list1[placechoose] != "-":
                        print("Occupied already, Choose again")
                        continue
                except ValueError:
                    print("Not a valid value, choose 1 to 9 like on the board")
                break
            list1[placechoose] = endingpattern
            break
        if checkforwin(list1) == 1 or check_for_a_tie(list1) == 1:
            break


print("Welcome to TicTacToe")
print("Choose: ")
print("1. Against PC ")
print("2. Against another player ")

while True:
    try:
        against: int = int(input(""))
        if against != 1 and against != 2:
            print("Not a valid number, Choose again")
            continue
    except ValueError:
        print("Not a valid Value, Choose again")
        continue
    break

if against == 1:
    playervspc(list1,list2)
else:
    playervsplayer(list1,list2)

print("ENDING BOARD")
print(f"             I            I             ")
print(f"      {list1[1]}      I     {list1[2]}      I      {list1[3]} ")
print(f"             I            I             ")
print(f"----------------------------------------")
print(f"             I            I             ")
print(f"      {list1[4]}      I     {list1[5]}      I      {list1[6]} ")
print(f"             I            I             ")
print(f"----------------------------------------")
print(f"             I            I             ")
print(f"      {list1[7]}      I     {list1[8]}      I      {list1[9]} ")
print(f"             I            I             ")
print("Thank u for playing, Goodbye")

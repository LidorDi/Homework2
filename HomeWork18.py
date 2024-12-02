#1

tup1 = (99,)
tup2 = (99,88,77)

def tup_len (tup: tuple):
    return (len(tup))

def tup_tup(tup1 , tup2):
    return(tup1 + tup2)

def multtuple(tup1 , tup2):
    common: list = []
    for i in tup1:
        if i in tup2:
            common.append(i)
    return tuple(common)

def not_multtuple(tup1 , tup2):
    common: list = []
    for i in tup1:
        if i not in tup2:
            common.append(i)
    for i in tup2:
        if i not in tup1:
            common.append(i)
    return tuple(common)

def tup_index(tup1 , index1):
    return(tup1[index1])

def reversetup(tup1):
    return tup1[::-1]

def dubtup(tup1, num):
    return tuple(tup1 * num)

def noreturntup(tup1, num):
    list: [] = [i for i in tup1 if i != num]
    return tuple(list)

def nocommonlist(tup1):
    list: [] = []
    for i in tup1:
        if i not in list:
            list.append(i)
    return(tuple(list))

def tupindex(tup1 , num):
    list: [] = []
    index = 0
    for i in tup1:
        if i == num:
            list.append(index)
        index += 1
    return(list)

def tupdict():
    list1: [] = []
    list2: [] = []
    while True:
        str1: str = str(input("enter a name"))
        if str1 == "done":
            break
        list1.append(str1)
    while True:
        num1: int = int(input('enter a num'))
        if num1 == -999:
            break
        list2.append(num1)
    return (dict(zip(list1, list2)))

# the diffrence is that list can change according to the program but tuple not. u use tuple when u dont want any value to change all through the code, u use list when ull make some changes
# the code wont show an error beacuse its a dict inside a tuple, the tuple saves the value in the index of the dict as a dict and not as the value in the dict.


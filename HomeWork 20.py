

#############
###########
# I have been sitting the first task code for 1.5 hours or so if u can show me where i can make it more smooth itll help! ty (the brackets one)
##############
############

x: str = str(input("enter some brackets"))
openedbrackets = []
closedbrackets = []
for i in x:
    if i == "{" or i == "(" or i == "[":
        openedbrackets.append(i)
        continue
    if len(openedbrackets) == 0:
        print(False)
        break
    if i == "}" or i == "]" or i == ")":
        closedbrackets.append(i)
        continue
counter = len(openedbrackets)
counterreal = 0
while True:
    for i in openedbrackets:
        if i == "{" and closedbrackets[len(closedbrackets) - 1] == "}":
            openedbrackets.pop(0)
            closedbrackets.pop(len(closedbrackets) - 1)
            continue
        elif i == "[" and closedbrackets[len(closedbrackets) - 1] == "]":
            openedbrackets.pop(0)
            closedbrackets.pop(len(closedbrackets) - 1)
            continue
        elif i == "(" and closedbrackets[len(closedbrackets) - 1] == ")":
            openedbrackets.pop(0)
            closedbrackets.pop(len(closedbrackets) - 1)
            continue
    if counterreal > counter:
        break
    counterreal +=1

if len(closedbrackets) != 0 or len(openedbrackets) != 0:
    print(False)
else:
    print(True)

####################################################################
x1 = 0
list1: list = []
while True:
    x1 = int(input("enter a list memoanet . to exit enter a -999"))
    if x1 == -999:
        break
    list1.append(x1)
list2 = []
counter1 = min(list1)
while max(list1) >= counter1:
    for i in list1:
        if counter1 == i:
            list2.append(i)
    counter1 += 1
print(list2)

########################################################################

list5: list = []
while True:
    x2 = int(input("enter a list memoanet . to exit enter a -999"))
    if x2 == -999:
        break
    list5.append(x2)

list6: list = []
while True:
    x3 = int(input("enter a list memoanet . to exit enter a -999"))
    if x3 == -999:
        break
    list6.append(x3)

list7 = []

if min(list6) > min(list5):
    counterreal11 = min(list5)
else:
    counterreal11 = min(list6)
if max(list6) > max(list5):
    sentinel = max(list6)
else:
    sentinel = max(list5)
while sentinel >= counterreal11:
    for i in list5:
        if counterreal11 == i:
            list7.append(i)
    for i in list6:
        if counterreal11 == i:
            list7.append(i)
    counterreal11 += 1
print(list7)


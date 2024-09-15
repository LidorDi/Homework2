# Assignment 1

slices: int = int(input("how much slices of pizza"))
sliceseachone: int = slices // 4
leftovers: int = slices % 4
if leftovers != 0:
    print(f" {sliceseachone} slices for each member and {leftovers} slices left")
else:
    print(f"{sliceseachone} slices for each member ")

#######################################################

members: int = int(input("How much members are coming?"))
slices1: int = int(input("how much slices of pizza"))
slicesforeach: int = slices1 // members
leftovers1: int = slices1 % members

if leftovers1 != 0:
    print(f" {slicesforeach} slices for each member and {leftovers1} slices left")
else:
    print(f"{slicesforeach} slices for each member ")

# Assignment 3

# if 4 < 9: FALSE
# if (2 * 3 + 4) * (7 + 7): TRUE
# if 18 + 18: TRUE
# if 10 == 10: TURE
# if 10 == 10 and 20 == 30: FALSE
# if 10 == 10 or 20 == 30: TRUE
# if 20 == 30 or 10 == 10: TRUE
# if not 3: FALSE
# if 3: TRUE
# if (33 > 20) and (2 < 12) and 10: TRUE
# if TRUE and TRUE: TRUE
# if TRUE and FALSE: FALSE
# if TRUE or FALSE: TRUE
# if FALSE or TRUE: TRUE
# if (not 10) and (10): FALSE
# if (not 10) and (not 10): FALSE
# if 5 != 5 and 5 == 5: FALSE
# if 2 == 2 or 3 == 3: TRUE
# if 2 == 2 and 3 == 3: TRUE
# if 40 == 30 and 1 >= 4: FALSE
# if 13 >= 3 or 47 >= 5: TRUE

# Assignment 4

x: int = 10
while (x <= 20):
    print(x)
    x += 1

##################################################################

y: int = 10
while (y <= 20):
    print(y)
    y += 2

##################################################################

o: int = 10
z: int = int(input("Enter the how much steps"))
while (o <= 20):
    print(o)
    o += z


a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 3
d = 3
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 1
d = 1
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 0
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 1
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 5
b = 2
c = 1
if a != b and a <= c or a <= b or True: ####################### אי אפשר לשנות
     print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 5
b = 3
c = 1
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 3
c = 0
d = 0
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")
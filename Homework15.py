from html.parser import starttagopen
from random import random

# 1

# list1: list[int] = []
# for _ in range (100):
#     x : int = random.randint(1, 100)
#     list1.append(x)
#
# list(filter(lambda x: x > 50 , list1))
# list(filter(lambda x: x % 7 == 0 , list1))
# list(filter(lambda x: x > 9 , list1))
# list(filter(lambda x: x % 10 == x // 10 , list1))
# list(filter(lambda x: x % 10 + x // 10 == 9 , list1))
# list(filter(lambda x: x > sum(list1) / 100 , list1))
# list(filter(lambda x: x > (max(list1)//2) , list1))

#2

# list2 = ["V Auto Theft Grand ","Fortnite","The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
# print(list(filter(lambda x: len(x) > 8 , list2)))
# print(list(filter(lambda x: x.upper().startswith("F") , list2)))
# print(list(filter(lambda x: len(x.split()) == 2 , list2)))
# print(list(filter(lambda x: "V" in x.upper() , list2)))


#3

# list3: list[int] = []
# for _ in range (20):
#     x: int = random.randint(-50,50)
#     list3.append(x)
# print(list(map(lambda x: x**3 , list3))) # randint לא עובד אצלי אז אין לי אופציה לבדוק
# print(list(map(lambda x: x % 10 , list3)))
# print(list(map(lambda x: x* 5 + 32 , list3)))
# print(list(map(lambda x: "positive" if x > 0 else "negative"  , list3)))

#4

# list4: list[str] = ["Mango","Orange","Banana","Apple" ,"Strawberry", "Pineapple", "Grapes", "Watermelon"]
# print(list(map(lambda x: x[::-1] , list4 )))
# print(list(map(lambda x: x[:1:] , list4 )))
# print(list(map(lambda x: x[len(x)//2 - 1:len(x)//2 :] , list4 )))
# print(list(map(lambda x: x + "!" if x.upper().endswith("S") else x, list4 )))

#5

# המשמעות היא שהוא המספר המרכזי של ערך מסויים. כשאצור פונקציה ובה לא ימצא ערך צרוך הוא יילך לערך הגלובלי וייקח משם את
# פקודות מסויימות יכולות לתת ערך שונה לערך הגלובלי

# נקבל שגיאה כי אין ערך לx

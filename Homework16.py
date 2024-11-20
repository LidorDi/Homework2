# 1

from random import random

list1 = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

print(sorted(list1 , key = lambda w: len(w)))
print(sorted(list1 , key = lambda w: len(w.split())))
print(sorted(list1 , key = lambda w: w[:len(w):]))
print(sorted(list1 , key = lambda w: w[::-1]))
print(sorted(list1 , key = lambda w: w.count("a")))


list2 = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]

# print(sorted(list2 , key = lambda w: w[1]))
# print(sorted(list2 , key = lambda w: w[1] , reverse = True))
# print(sorted(list2 , key = lambda w: w[2]))
# print(sorted(list2 , key = lambda w: w[2][1]))

# list3: list[int] = []
# for _ in range (50):
#     x : int = random.randint(1, 100)
#     list3.append(x)
#
# print(sorted(list3))
# print(sorted(list3 , key = lambda w: sum(list3))) # לא יכול לבדוק לצערי, random לא עובד לי, מחקתי והתקנתי pycharm מחדש ועדיין לא עובד

#2

sentence = " This chocolate cake is rich, moist, and full of delicious chocolate flavor To make the cake you will need chocolate flour sugar  eggs and butter After baking the chocolate cake let the cake cool before adding the chocolate frosting"
sentence1 = sentence.split()
word_sent: dict[str: int] = {}
word_sent1: dict[str: int] = {}
for word in sentence:
    word_sent[word] = word_sent.get(word, 0) +1
for word in sentence1:
    word_sent1[word] = word_sent1.get(word, 0) +1
print(max(word_sent))
print(min(word_sent1))

#3

num_sent: dict[int: int] = {}
for i in range (1,21):
    num_sent.update({i : i**3})
x: int = int(input("enter a number"))
print(num_sent.get(x, "not valid"))



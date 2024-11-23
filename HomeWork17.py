
israeldict: dict = {"name": "israel",
                    "birth": 1948,
                    "population_millions": 9.3,
                    "capital": "jerusalem",
                    "language": "hebrew",
                    "cities": "jerusalem , tel aviv , haifa , rhison lezion , petah tikva , ashdod",
                    "currency": "ils",
                    "area_kilometer": 22145,
                    "gdp_billion": 450}
print(israeldict.get("capital"))
print(israeldict.keys())
print(israeldict.values())
for a,b in israeldict.items():
    print(f"{a} : {b}")
israeldict1 =israeldict.copy()
israeldict1.pop("gdp_billion")

israeldictnew = israeldict.fromkeys(("name" , "birth" , "population_millions" , "capital" , "language" ,"cities","currency","area_kilometer", "gdp_billion" ))
for i in israeldictnew:
    if i == "cities":
        x = input("give me a city")
        b = input("give me another city")
        c = input("give me a third city")
        israeldictnew[i] = f"x , b , c"
    else:
        israeldictnew[i] = input(f"what is the {i}")
print(israeldictnew)


# last word of a string

word = str(input("enter a string of words"))
word1 = word.split()
print(len(word1[len(word1) - 1]))
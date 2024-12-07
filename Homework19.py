oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson")
oscarduplicate: set = oscar_winners.copy()
oscarduplicate.remove("Meryl Streep")
oscarduplicate.clear()
print(titanic_actors & dark_knight_actors)
print(bool(iron_man_actors & avengers_actors))
print(actor_list >= oscar_winners)
print(actor_list >= avengers_actors)
movie_cast.pop()
movie_cast.remove("Matt Damon")
print(titanic_actors.difference(oscar_winners))
print(f"{titanic_actors.difference(dark_knight_actors)} only on titanic")
print(f"{dark_knight_actors.difference(titanic_actors)} only on dark knight")
oscar_winners.add("Daniel Day-Lewis")
oscar_winners.add("Cate Blanchett")
print(dark_knight_actors.update(titanic_actors))


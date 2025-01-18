# 7. ?
# DELETE from shopping WHERE name like 'Orange';

# where The name = orange it will delete the row


# 8. ?
# UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
# UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'

# first one changes the name = bisli to name = bamba
# second is changing the amount to 1 where the name is "milk"


# 9. ?
# ALTER TABLE shopping ADD COLUMN maavar

# it adds a new row named "maavar"

# 10. ?
# UPDATE shopping SET maavar=6 WHERE id=1;
# UPDATE shopping SET maavar=3 WHERE id=2;
# UPDATE shopping SET maavar=12 WHERE id=3;
# UPDATE shopping SET maavar=8 WHERE id=4;
# UPDATE shopping SET maavar=5 WHERE id=5;

#changes the maavar value according to specific ids

# 11. ?
# SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
# SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5

#first one selects the only rows that the value amont is bigger than 1 and maavar bigger than 5
# second is seclecting only the rows where maavar value is between 3 - 5

# 12. ?
# SELECT * FROM shopping ORDER BY maavar
# SELECT * FROM shopping ORDER BY maavar DESC

#first one is sorting the rows by maavar values (acending as defult)
#second one is sorting it same as maavar values but as descending

# 13. ?
# CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
# INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
# INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
# DELETE FROM books;

#it makes a new table named books with id that is int and primary + name that is text
# second is inserting the id = 1 and name = sql programming
#third is inserting the values id = 2 name = csharp programming
# deletes all of the rows in the table but doesnt delete the table itself

# 14. ?
# SELECT COUNT(*)from shopping
# SELECT MAX(amount) from shopping
# SELECT AVG(amount) from shopping
# SELECT MIN(amount) from shopping

# it counts the rows in shopping table
#it shows the rows with the highest amount
# same but the avrage amount
# sane but the minimum amount

# 15. ?
# INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
# INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
# Select maavar, COUNT(*)FROM shopping GROUP BY maavar

#it adds the values to shopping on the first column - 6 second "onions" third 3 and last 6
# same but with diffrent values
# it groups the same values of "maavar" as one and shows them in groups and shows the count of the rows in the table

# 16. ?
# SELECT id AS "SECRET", name, amount, maavar FROM shopping

# it shows the id but changes its name to secret (temporary) shows name amount and maavar regularly

#1. Create/Drop table:
# CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
# INTEGER);
# DROP TABLE shopping

# 1. it makes a new table named shopping with id as a primary key which is int, name which is char and amount which is int and then it deletes the table


# 2. Rename table:
# ALTER table shopping RENAME to shopp
# ALTER table shopp RENAME to shopping

# it changes the name of the table to shopp and then back to shopping

# 3. Insert rows into table:
# INSERT INTO shopping VALUES (1, 'Avokado', 5);
# INSERT INTO shopping VALUES (2, 'Milk', 2);
# INSERT INTO shopping VALUES (3, 'Bread', 3);
# INSERT INTO shopping VALUES (4, 'Chocolate', 8);
# INSERT INTO shopping VALUES (5, 'Bamba', 5);
# INSERT INTO shopping VALUES (6, 'Orange', 10);

# it inserts values to the rows in the table in the same order as the rows for examble in line 1: 1 will go into the first row in the table

# 4. Display table:
# select * from shopping

# shows every vavlue in the table


# 5. ?
# SELECT id, name FROM shopping

# shows the exact value that u asked for which in this case is id from the table "shopping"

# 6. ?
# SELECT * FROM shopping WHERE amount > 5
# SELECT * FROM shopping WHERE amount = 2
# SELECT * FROM shopping WHERE name LIKE 'Bamba'

# it goes over all the values and bring back only the ones that are bigger than 5 in the first only that equal to 2 in the scond and only that the text in them is Bamba in the third
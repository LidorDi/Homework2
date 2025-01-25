import sqlite3
import os

###################################### SEEN IN THE END THE OS IF I HAD SEEN IT SOONNER THE TRY, EXECPT SHOULDNT BE NEEDED
db_name: str = "dsf.db"
if os.path.exists(db_name):
    print("there is an gets removed")
    os.remove(db_name)
else:
    print("doesnt exist")
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER)")
except: pass

tuple1 =((1, 'Avokado', 5) , (2, 'Milk', 2) , (3, 'Bread', 3) , (4, 'Chocolate', 8) , (5, 'Bamba', 5) , (6, 'Orange', 10) )

try:
    cursor.executemany("INSERT INTO shopping (id, name, amount) VALUES (?, ?, ?)", tuple1)
except: pass
conn.commit()


cursor.execute("SELECT * FROM shopping")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))

print("")

cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))

print("")

try:
    cursor.execute("DELETE from shopping WHERE name like 'Orange'")
except: pass
conn.commit()

try:
    cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
    conn.commit()
    cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")
    conn.commit()
except: pass

cursor.execute("SELECT COUNT(*)from shopping")
rows1 = cursor.fetchall()
for row in rows1:
    print(dict(row))
print("")
cursor.execute("SELECT * FROM shopping WHERE id > 0")
rows1 = cursor.fetchall()
for row in rows1:
    print(dict(row))

conn.close()
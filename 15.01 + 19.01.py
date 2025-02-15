import sqlite3

db_name: str = "dsf.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

#a

cursor.execute("CREATE TABLE IF NOT EXISTS category (category_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price INTEGER NOT NULL, category_id INTEGER, FOREIGN KEY (category_id) REFERENCES category(category_id) )")
cursor.execute("CREATE TABLE IF NOT EXISTS nutritions (nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER , name TEXT NOT NULL , calories INTEGER NOT NULL, fats INTEGER NOT NULL, sugar INTEGER NOT NULL, FOREIGN KEY (product_id) REFERENCES products(product_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT, date_time INTEGER NOT NULL, address TEXT NOT NULL, customer_name TEXT NOT NULL, customer_ph INTEGER NOT NULL, total_price INTEGER NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS products_orders (order_id INTEGER, product_id INTEGER, amount INTEGER NOT NULL, PRIMARY KEY (order_id , product_id), FOREIGN KEY (order_id) REFERENCES orders(order_id), FOREIGN KEY (product_id) REFERENCES products(product_id))")
conn.commit()

#b

#1 to many

#c
#from now on I did on sql

#d1

#SELECT category.name as Category_Name , products.name as Product_Name , nutritions.calories as calories , nutritions.fats As fats , nutritions.sugar AS sugar FROM products
#JOIN nutritions ON nutritions.product_id = products.product_id
#JOIN category ON category.category_id = products.category_id
#ORDER BY category.name

#d2

#SELECT products_orders.order_id , category.name , products.name , products.price ,products_orders.amount from products
#JOIN products_orders ON products_orders.product_id = products.product_id
#JOIN category ON category.category_id = products.category_id
#ORDER BY products_orders.order_id

#d3

#INSERT INTO products_orders (order_id , product_id, amount) VALUES
#(1 , 13 , 2),
#(2, 13 , 1),
#(3 , 15 ,2),
#(4, 10 ,3),
#5, 12 , 4)

#d4

#UPDATE orders
#SET total_price = (
#SELECT SUM(products.price * products_orders.amount)
#FROM products_orders
#JOIN products ON products_orders.product_id = products.product_id
#WHERE products_orders.order_id = orders.order_id

#d5

#SELECT * FROM orders
#ORDER BY total_price DESC
#LIMIT 1;

#d6

#SELECT customer_name, COUNT(id_order) AS order_count
#FROM orders
#GROUP BY customer_name
#ORDER BY order_count DESC
#LIMIT 1;

#d7

#SELECT products.name, SUM(products_orders.amount) AS total_sold
#FROM products
# JOIN products_orders ON products.product_id = products_orders.product_id
# GROUP BY products.name
# ORDER BY total_sold DESC
# LIMIT 1;

#d8

# SELECT category.name, SUM(products_orders.amount * products.price) AS total_sales
# FROM category
# JOIN products ON products.category_id = category.category_id
# JOIN products_orders ON products.product_id = products_orders.product_id
# GROUP BY category.name
# ORDER BY total_sales DESC
# LIMIT 1;

#d9

# SELECT products.name, COUNT(products_orders.order_id) AS order_count
# FROM products
# JOIN products_orders ON products.product_id = products_orders.product_id
# GROUP BY products.name
# ORDER BY order_count DESC
# LIMIT 1;


conn.close()
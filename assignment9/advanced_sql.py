import sqlite3

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

try:
  #Task 1: Complex JOINs with Aggregation
  query1 = """
  SELECT o.order_id, SUM(p.price * li.quantity) 
  FROM orders AS o 
  JOIN line_items AS li ON o.order_id = li.order_id
  JOIN products AS p ON li.product_id = p.product_id
  GROUP BY o.order_id
  ORDER BY o.order_id
  LIMIT 5
  """
  cursor.execute(query1)
  print(cursor.fetchall())

  #Task 2: Understanding Subqueries
  query2 = """
  SELECT c.customer_name, AVG(total_price) AS average_total_price  
  FROM customers as c
  LEFT JOIN (
    SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price 
    FROM orders AS o 
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
  ) ON c.customer_id = customer_id_b
  GROUP BY customer_id
  """
  cursor.execute(query2)
  print(cursor.fetchall())

  #Task 3: An Insert Transaction Based on Data
  query3a = """
  SELECT customer_id
  FROM customers 
  WHERE customer_name = 'Perez and Sons'
  """
  cursor.execute(query3a)
  target_customer_id = cursor.fetchone()[0]

  query3b = """
  SELECT product_id
  FROM products 
  ORDER BY price ASC
  LIMIT 5
  """
  cursor.execute(query3b)
  target_product_ids = cursor.fetchall()
  
  query3c = """
  SELECT employee_id
  FROM employees 
  WHERE first_name = 'Miranda' AND last_name = 'Harris'
  """
  cursor.execute(query3c)
  target_employee_id = cursor.fetchone()[0]

  # create the order record 
  cursor.execute("INSERT INTO orders (customer_id, employee_id, date) VALUES (?,?,?) RETURNING order_id", (target_customer_id, target_employee_id, '2026-01-26'))
  target_order_id = cursor.fetchone()[0]

  # create 5 line_item records
  for product_id in target_product_ids:
    cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?,?,?)", (target_order_id, product_id[0], 10))

  # print the result
  query3result = """
  SELECT li.line_item_id, li.quantity, p.product_name 
  FROM line_items li
  JOIN products p ON li.product_id = p.product_id
  WHERE li.order_id = ?
  """
  cursor.execute(query3result, (target_order_id,))
  print(cursor.fetchall())


  #Task 4: Aggregation with HAVING
  query4 = """
  SELECT e.first_name, e.last_name, COUNT(o.order_id)
  FROM employees e
  JOIN orders o ON e.employee_id = o.employee_id
  GROUP BY e.employee_id
  HAVING COUNT(o.order_id) > 5 
  """
  cursor.execute(query2)
  print(cursor.fetchall())

  conn.commit()
  conn.close()

except Exception as e:
  conn.rollback()
  print("Error: ", e)

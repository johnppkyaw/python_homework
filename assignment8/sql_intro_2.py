import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    
    #The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and the product table.
    sql_statement = """SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df[:5])
    df['total'] = df['quantity'] * df['price']
    print(df[:5])
    
    #Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, and 'first' for the 'product_name'
    agg_obj = {
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }
    grouped_df = df.groupby('product_id').agg(agg_obj)
    print(grouped_df[:5])
    grouped_df = grouped_df.sort_values(by='product_name')
    grouped_df.to_csv('order_summary.csv', index=False)
    

 
    

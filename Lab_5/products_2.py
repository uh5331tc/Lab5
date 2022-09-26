import sqlite3

#validation error Row ID


db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT) ')
conn.close()

name = 'boots'
quantity = 1

try:
    with sqlite3. connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?, ?)', (name, quantity))
    conn.close()
except Exception as e:
        print('Error Inserting', e)


conn = sqlite3.connect(db)
results = conn.execute('SELECT rowid, * FROM products')  #row id will get primary key 

for row in results:
    print(row)

conn.commit()  #required 

print('end of program ')


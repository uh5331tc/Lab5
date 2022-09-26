import sqlite3

db = 'first_db.sqlite'


def create_table():
    with sqlite3.connect(db) as conn:  #use 'db' the variable name        conn.execute('CREATE TABLE products (id int, name text)')  #create table if not exists
        #conn.execute('DROP TABLE products')  #create table if not exists
        conn.execute('CREATE TABLE products (id int, name text)')  #create table if not exists
    conn.close()

def insert_exapmle_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (100, "hat")')
        conn.execute('INSERT INTO products values (200, "boot")')
    conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    print('All products: ')
    for row in results:
        print(row) #each row is a tuple
        #print(row[1])  # each row is a raw object
    conn.close()

def display_one_product(product_name):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like ?', (product_name,)) ## ADD COMMA
    first_row = results.fetchone()
    if first_row:
        print('not found')
    print('Your product is: ', first_row) # upgrade to row factory later???
    conn.close(  )

def create_new_product():
    new_id = int(input('enter new id: '))
    new_name = input('enter new product: ')

    with sqlite3.connect(db) as conn:  #use 'db' the variable name
        conn.execute(f'INSERT INTO products VALUES (? , ?)',  (new_id, new_name) )
    conn.close()

def update_product():
    updated_product = 'hat'
    update_id = 100

    with sqlite3.connect(db) as conn:  #use 'db' the variable name
        conn.execute('UPDATE products SET name = ? WHERE id = ? ', (updated_product, update_id ) )
    conn.close()

def delete_product():
    with sqlite3.connect(db) as conn:  #use 'db' the variable name
        conn.execute('DELETE from products WHERE name = ?', (delete_product, ) ) #must have comma if only one
    conn.close()

        #conn will automatically commit() when inside the 'with' block


create_table()
insert_exapmle_data()
display_all_data()
display_one_product('hat')
create_new_product()
update_product()
delete_product()
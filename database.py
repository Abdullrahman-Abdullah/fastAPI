import sqlite3

conn = sqlite3.connect('products_database.db')

cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                price TEXT,
                count INTEGER  
               )

'''
)

# cursor.execute(""" 
#     INSERT INTO product ( name, description, price, count ) VALUES  (?, ?, ?, ?)
# """,
# ("switch", "for 220 volt", "2.4$", 50))
# conn.commit()




cursor.execute("UPDATE product SET name = ? ,description = ?, price = ?, count = ? WHERE id = ?", ("mqbs", "for dc battery", "9.4$", 30, 1))
conn.commit()

get_all_product = cursor.execute("SELECT * FROM product").fetchall()
print(get_all_product)


cursor.execute("DELETE FROM product WHERE id =? ", (8,))
conn.commit()


conn.close()
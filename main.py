from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: str
    count: int

app = FastAPI()


@app.get("/product")

async def AllProduct():
            
            try:
                conn = sqlite3.connect('products_database.db')
                cursor = conn.cursor()
                products = cursor.execute("SELECT * FROM product")
                row = cursor.fetchall()
                conn.close()
                return row
                
            except:
                    return {"Error Massage": "something went wrong"}
   


@app.post("/product")

async def NewProduct(Product: Product):
        try:
                conn = sqlite3.connect('products_database.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO product (name, description, price, count) VALUES (?,?,?,?)", (Product.name , Product.description, Product.price , Product.count))
                conn.commit()
                conn.close()
                return {"Massage": "product added successfully"}
        except sqlite3.Error as e:
                print(e)
                return {"Error Masaage": "Error adding product `${e}`"}
        
@app.put("/product/{product_id}")
async def Update_Product(product_id: int , product: Product):
       try:
              conn = sqlite3.connect('products_database.db')
              cursor = conn.cursor()
              cursor.execute("UPDATE product SET name = ? , description = ?, price = ? , count = ? WHERE id =?",
                             (product.name , product.description , product.price , product.count, product_id))
              conn.commit()
              conn.close()
              return {"id" : product_id , **product.dict()}
       except sqlite3.Error as e:
              print(e)
              return {"Error Massage": "Update is unable try again later"}
       
@app.delete("/product/{product_id}")

async def Delete_Product(product_id: int ):
       try: 
              conn = sqlite3.connect('products_database.db')
              cursor = conn.cursor()
              cursor.execute("DELETE FROM product WHERE id = ? ", (product_id,))
              conn.commit()
              conn.close()
              return {"product of this id was deleted": product_id }
       except sqlite3.Error as e:
              print(e)
              return {"Error Massage": "delete this product is unable now please try again later"}

#Michelle Yick
#27/04/2015
#Searching and sorting data - Task 7 - Python school

import sqlite3

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor=db.cursor()
        cursor.execute("select * from Product") #Star (*) is a wildcard that represents all attributes
        products=cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor=db.cursor()
        cursor.execute("select Name,Price from Product where ProductID=?",(id,)) #Name and price will only return the name and price of product. A * will return all the products
        product=cursor.fetchone()
        return product

if __name__=="__main__":
    products=select_all_products()
    print(products)
    product=select_product(2)
    print(product)


#Michelle Yick
#23/04/2015
#Inserting data into a product table - Python school - Task 3

import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor=db.cursor()
        sql="insert into Product (Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit

if __name__=="__main__":
    product=("Espresso",1.5)
    insert_data(product)

insert_data()


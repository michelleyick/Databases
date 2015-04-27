#Michelle Yick
#23/04/2015
#Deleting data - Python school - Task 5

import sqlite3

def delete_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor=db.cursor()
        sql="delete from Product where Name=?"
        cursor.execute(sql,data)
        db.commit()

if __name__=="__main__":
    data=("Americano",)
    delete_product(data)

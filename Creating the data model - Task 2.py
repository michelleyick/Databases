#Michelle Yick
#20/04/2015
#Creating a new product table and improving it - Python school - Task 2

#Edit the program from task 1 so that it doesn't produce an error message.

import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name)as db:
        cursor=db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,)) #detect whether or not the product table already exists
        result=cursor.fetchall() #gets the results
        keep_table=True
        if len(result)==1:
            response=input("The table {0} already exists, do you wish to recreate it (y/n):".format(table_name))
            if response=="y":
                keep_table=False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table=False
        if not keep_table:
            cursor.execute(sql)
            db.commit() #to commit a change

if __name__=="__main__":
    db_name="coffee_shop.db"
    sql="""create table Product
           (ProductID integer,
           Name text,
           Price real,
           primary key(ProductID))"""
    create_table(db_name,"Product",sql)

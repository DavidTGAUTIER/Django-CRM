# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysqldev'
)

# prepare a cursor object 
cursor_object = database.cursor()

# create a database

cursor_object.execute("CREATE DATABASE david_db")

print("All Done !")


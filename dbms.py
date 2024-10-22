# python -m pip install mysql-connetor-python
# py -m pip install mysql-connetor-python

import mysql.connector
# start by creating a connection to the database
# establish a connection to the mysql server using the conncet() method.
# you need to provide connection details such as the host , user, password and database
# pip is package manager of python
# 3306 default port number

data = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database=""
)
print("connected")

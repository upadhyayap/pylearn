# There are two popular package for ODBC in Python:
# pyodbc: This package uses ODBC Driver Manager and connects to your database using ODBC driver. It is a wrapper around ODBC driver.
# pypyodbc: This package is similar to pyodbc but is written entirely in Python and does not require any libraries to work.

import pymongo
from sqlalchemy import create_engine
import sqlalchemy as sal
import mysql.connector
import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'SERVER=localhost: 1433'
port = 'PORT=1433'
db = 'DATABASE=main'
user = 'UID=root'
pw = 'PWD= Educative@123'

conn_str = ([driver, server, port, db, user, pw])
c = ['DRIVER={ODBC Driver 17 for SQL Server}', 'SERVER=localhost: 1433',
     'DATABASE=main', 'UID=root', 'PWD= Educative@123']
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;UID=sa;PWD=Educative@123')

cursor = conn.cursor()
cursor.execute('select * from table_name')
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
print(rest_of_rows)


# using mysql-connector

conn = mysql.connector.connect(
    host='localhost', user='educative', password='secret', database='test')
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# get a single row
row = cursor.fetchone()
print('printing the first row:')
print(row)

# disconnect from the database
conn.close()


# nost popular ORM in Python is SQLAlchemy
# SQLAlchemy is a Python library that provides a SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
# connection format: dialect+driver://username:password@host:port/database
engine = create_engine(
    "postgresql+psycopg2://educative:secret@localhost:5432/test")
conn = engine.connect()
cursor = conn_sql.cursor()
print(engine)
# execute a query
cursor.execute("SELECT * FROM table_name;")
row = cursor.fetchone()
print(row)
# close your cursor and connection
cursor.close()
conn.close()


# mongo: pip3 install pymongo

client = pymongo.MongoClient("mongodb://localhost:3000/")
# creating database
database = client["mongodatabase"]
# creating collection
collection = database["mongocollection"]
collection.insert_one({"name": "John", "address": "Highway 37"})
collection.delete_one({"address": "Highway 37"})

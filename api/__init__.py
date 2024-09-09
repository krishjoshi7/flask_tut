import psycopg2
from flask_cors import CORS
from flask import Flask
dbname = 'Test_Data_base'
host = 'localhost'
user = 'postgres'
password = '121002'
port = 5432
connection = psycopg2.connect(host = host,dbname = dbname,user = user,password = password,port = port)
cur = connection.cursor()
connection.autocommit = True
#creazione di una tabella
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Manethdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE calciatori (name VARCHAR(255), number VARCHAR(255))")
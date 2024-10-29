#selezionare dei dati di una tabella
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Manethdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM calciatori")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
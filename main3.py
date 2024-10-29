#inserire dei dati in una tabella
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Manethdatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO calciatori (name, number) VALUES (%s, %s)"
val = [
  ('Cristiano Ronaldo', '7'),
  ('Neymar jr', '11'),
  ('Kylian Mbappe', '9'),
  ('Sergio Ramos', '4')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
#creazione di un database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("USE Animali")
mycursor.execute("CREATE TABLE IF NOT EXISTS mammiferi (id INT PRIMARY KEY AUTO_INCREMENT, Nome_proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")

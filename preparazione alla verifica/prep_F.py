import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()
risp = "",
rispOpz = int(input("1) Aggiungi un nuovo mammifero - 2) Visualizza la tabella  ")) 
quantMammiferi = int(input("Quanti mammiferi vuoi aggiungere alla tabella? ")) 
for _ in range(quantMammiferi):
  if(rispOpz == 1):
    mycursor.execute("USE Animali")
    Nome = input("Inserisci il nome: ")
    Razza = input("Inserisci la razza: ")
    while True:
            try:
                Peso = float(input("Inserisci il peso: "))  # Peso come float
                break
            except ValueError:
                print("Errore: inserisci un numero valido per il peso.")
    while True:
            try:
                Eta = int(input("Inserisci l'età: "))  # Età come intero
                break
            except ValueError:
                print("Errore: inserisci un numero intero valido per l'età.")
    sql = "INSERT INTO mammiferi (Nome_proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    val = (Nome, Razza, Peso, Eta)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
  elif (rispOpz == 2):
    mycursor.execute("USE Animali")
    mycursor.execute("SELECT * FROM mammiferi")
    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
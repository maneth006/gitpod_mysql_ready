import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()

rispOpz = int(input("1) Aggiungi un nuovo mammifero - 2) Visualizza la tabella - 3) Elimina un mammifero - 4) Modifica un mammifero ")) 
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

elif (rispOpz == 3):
    risp_id3 = int(input("Inserisci l'id dell'animale che vuoi eliminare:  ")) 

    mycursor.execute("USE Animali")
    querydelete = "DELETE FROM mammiferi WHERE id = %s"
    mycursor.execute(querydelete, (risp_id3,))
    mydb.commit()

elif (rispOpz == 4):
    risp_id3 = int(input("Inserisci l'id dell'animale che vuoi modificare:  ")) 
    mycursor.execute("USE Animali")
    NomeM = input("Inserisci il nome: ")
    RazzaM = input("Inserisci la razza: ")
    while True:
            try:
                PesoM = float(input("Inserisci il peso: "))  # Peso come float
                break
            except ValueError:
                print("Errore: inserisci un numero valido per il peso.")
    while True:
            try:
                EtaM = int(input("Inserisci l'età: "))  # Età come intero
                break
            except ValueError:
                print("Errore: inserisci un numero intero valido per l'età.")
    queryupdate = "UPDATE mammiferi SET Nome_proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE id = %s"
    valori = (NomeM, RazzaM, PesoM, EtaM, risp_id3)
    mycursor.execute(queryupdate, valori)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

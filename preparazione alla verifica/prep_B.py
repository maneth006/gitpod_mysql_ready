import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mammiferi (id, Nome_proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('1', 'Leo', 'Leone (Panthera leo)', '190','8'),
    ('2', 'Bella', 'Elefante africano (Loxodonta africana)', '6000','25'),
    ('3', 'Max', 'Lupo grigio (Canis lupus)', '40','5'),
    ('4', 'Daisy', 'Canguro rosso (Macropus rufus)', '85','6'),
    ('5', 'Oliver', 'Orso bruno (Ursus arctos)', '300','10')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
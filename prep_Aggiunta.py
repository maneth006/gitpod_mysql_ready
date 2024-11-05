#main.py
# Import the Flask module that has been installed.
import mysql.connector
from flask import Flask

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()


# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
mycursor.execute("SELECT * FROM mammiferi")

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()
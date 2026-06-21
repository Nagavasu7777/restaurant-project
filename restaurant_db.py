import mysql.connector

conn = mysql.connector.connect(

    host ="localhost",
    user = "root",
    database = "palnadu_restaurant",
    password = "Vasu@5351"
)

cursor = conn.cursor()


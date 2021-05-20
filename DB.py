import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RRROOOTTT12345",
    database="familytreedb"
)

mycursor = db.cursor()
import mysql.connector
class ConexionDb:
    def __init__(self):
        conexion = mysql.connector.connect(user="root", 
                                        password="123456", host="localhost", 
                                        database="bd_yesid_david_martinez_arrieta", port=3306)
        print(conexion)

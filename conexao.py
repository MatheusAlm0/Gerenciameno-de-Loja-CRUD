import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user=" ",
        password=" ",
        database="db_sistema"
    )
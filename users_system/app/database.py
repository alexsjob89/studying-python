import sqlite3

from config import DATABASE_NAME

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row
    
    return connection



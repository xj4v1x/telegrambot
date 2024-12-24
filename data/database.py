# Interacción con bases de datos (si usas una)

import sqlite3

def get_connection():
    conn = sqlite3.connect("bot_data.db")
    return conn

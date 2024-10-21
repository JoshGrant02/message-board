import mysql.connector
from datetime import datetime

def create_message(message: str, createdWhen: datetime, createdWho: str):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'messageboard'
    }
    connection = mysql.connector.connect(**config)
    proc = 'CALL messageboard.message_i (%s, %s, %s)'
    cursor = connection.cursor()

    cursor.execute(proc, (message, createdWhen, createdWho))
    connection.commit()

    cursor.close()
    connection.close()

    return

def get_messages():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'messageboard'
    }
    connection = mysql.connector.connect(**config)
    proc = 'SELECT messageId, message, createdWhen, createdWho FROM message'
    cursor = connection.cursor()

    messages = []

    cursor.execute(proc)
    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    messages = [{column: row[i] for i, column in enumerate(columns)} for row in results]

    cursor.close()
    connection.close()

    return messages

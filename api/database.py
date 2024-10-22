import mysql.connector
from datetime import datetime
import os

database_user = "root"
database_password = os.getenv("db_root_password")
database_db = os.getenv("db_name")
database_host = os.getenv("MYSQL_SERVICE_HOST")
database_port = int(os.getenv("MYSQL_SERVICE_PORT"))

def create_message(message: str, createdWhen: datetime, createdWho: str):
    config = {
        'user': database_user,
        'password': database_password,
        'host': database_host,
        'port': database_port,
        'database': database_db,
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.callproc('messageboard.message_i', args=(message, createdWhen, createdWho))
    connection.commit()

    cursor.close()
    connection.close()

    return

def get_messages():
    config = {
        'user': database_user,
        'password': database_password,
        'host': database_host,
        'port': database_port,
        'database': database_db,
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    messages = []

    cursor.callproc('messageboard.message_s')
    for result in cursor.stored_results():
        columns = [desc[0] for desc in result.description]
        for row in result.fetchall():  # Use fetchall() to get all rows
            messages.append({column: row[i] for i, column in enumerate(columns)})

    cursor.close()
    connection.close()

    return messages

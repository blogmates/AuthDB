#!/usr/bin/env python
import os
import psycopg2
import time
from psycopg2 import OperationalError

url = "db"
port="5432"

def create_database():
    retries = 0
    connected = False
    while not connected:
        try:
            # Connect to the default PostgreSQL database
            connection = psycopg2.connect(
                database="postgres",
                user="user",
                password="password",
                host=url,
                port=port
            )
            connected = True
            # connection.autocommit = True
            print("Connected to the default database")
            # Create a cursor object
            cursor = connection.cursor()

            # Create a new PostgreSQL database
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", ('authDB',))
            if not cursor.fetchone():
                cursor.execute("CREATE DATABASE authDB")
            # cursor = connection.cursor()
            # cursor.execute(f"CREATE DATABASE {os.getenv('POSTGRES_DB')};")
            cursor.close()

            # Close the connection
            #connection.close()

            # Connect to the newly created database
            connection_two = psycopg2.connect(
                dbname="authDB",
                user="user",
                password="password",
                host=url,
                port=port
            )
            # connection.autocommit = True

            # Create the users table
            cursor = connection_two.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    email VARCHAR(1024) PRIMARY KEY,
                    password VARCHAR(1024),
                    hash VARCHAR(1024)
                )
            """)
            connection_two.commit()
            cursor.close()

            print("Database and users table created successfully")

            # Close the connection
            connection_two.close()

        except OperationalError as e:
            print(f"The error '{e}' occurred. Retrying...")
            retries += 1
            connected = False
            time.sleep(5)

if __name__ == "__main__":
    create_database()

#!/usr/bin/env python
import os
import psycopg2
from psycopg2 import OperationalError

def create_database():
    try:
        # Connect to the default PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        # Create a new PostgreSQL database
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {os.getenv('POSTGRES_DB')};")
        cursor.close()

        # Close the connection
        connection.close()

        # Connect to the newly created database
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user="postgres",
            password=""
        )
        connection.autocommit = True

        # Create the users table
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE users (
                email VARCHAR(1024) PRIMARY KEY,
                password VARCHAR(1024),
                hash VARCHAR(1024)
            )
        """)
        cursor.close()

        print("Database and users table created successfully")

        # Close the connection
        connection.close()

    except OperationalError as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    create_database()

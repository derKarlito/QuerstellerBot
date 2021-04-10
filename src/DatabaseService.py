import mysql.connector
from mysql.connector import Error
import pyodbc

class DatabaseService:
    def __init__(self):
        self.connect()

    def connect(self):
        """ Connect to MySQL database """
        connection = None
        try:
            connection = mysql.connector.connect(host='localhost',
                                           database='QuerstellerUser',
                                           user='notyou',
                                           password='HiJk26.10')
            if connection.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)

        finally:
            return connection

    def insert(self,user):
        #TODO: Check for TypeError
        db = self.connect()
        cursor = db.cursor()
        sql = "INSERT INTO user (id, context, update) VALUES ("+user.id+", "+user.context+", "+user.update+")"
        try:
            # Executing the SQL command
            cursor.execute(sql)

            # Commit your changes in the database
            db.commit()

        except:
            # Rolling back in case of error
            db.rollback()

        # Closing the connection
        db.close()


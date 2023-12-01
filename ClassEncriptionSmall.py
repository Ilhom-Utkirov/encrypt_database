import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv
from models import test_crypt

Crypto = test_crypt.Crypto()

dotenv_path = join(dirname(__file__), 'dot.env')
load_dotenv(dotenv_path)

hosting = os.environ['DB_ENDPOINT']
user = os.environ['DB_USER']
passw = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']


class encription:
    test = ""

    def __init__(self):
        self.conn = object
        self.cursor = object
        self.response = ""

    # job_execution_son
    def selectDataTab33(self):
        try:
            self.conn = psycopg2.connect(host=hosting, user=user, password=passw, dbname=db_name)
            self.cursor = self.conn.cursor()
            query = "select id_job_exec_son, description " \
                    "from warehouse.job_execution_son;"

            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.response = results
        except(Exception, psycopg2.DatabaseError) as error:
            print("Error in transction Reverting all other operations of a transction ", error)
            self.conn.rollback()
        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()
                return self.response

    def updateTab33(self):
        try:
            self.conn = psycopg2.connect(host=hosting, user=user, password=passw, dbname=db_name)
            self.cursor = self.conn.cursor()
            lenResponse = len(self.response)
            for i in range(lenResponse):
                id_job_set = self.response[i][0]
                description = self.response[i][1]

                if description is not None:
                    description = Crypto.rot13(description)

                query = "UPDATE  warehouse.job_execution_son " \
                        "SET " \
                        "description = %s " \
                        "WHERE id_job_exec_son = %s;"

                self.cursor.execute(query, (description, id_job_set))

            self.conn.commit()
            self.response = "OK"

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error in transction Reverting all other operations of a transction ", error)
            self.conn.rollback()

        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()
                return self.response
            self.conn.commit()
            self.response = "OK"


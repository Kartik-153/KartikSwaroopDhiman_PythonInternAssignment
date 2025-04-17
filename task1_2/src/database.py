import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='app',
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))
    return conn 

import sqlite3, os, dotenv

dotenv.load_dotenv()
DATABASE = os.getenv('DATABASE')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def cursor():
    conn = get_connection()
    cur = conn.cursor()
    return cur
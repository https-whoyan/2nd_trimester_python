import psycopg2
from config import DB_PASS, DB_PORT, DB_NAME, DB_USER, DB_HOST


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def get_cursor():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn.cursor()
    except Exception as e:
        return None

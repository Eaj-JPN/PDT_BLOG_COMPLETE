import psycopg2


def db_connection():
    """ function to open connection """
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='db_assignment2',
        user='postgres',
        password='20072004'
    )
    return conn

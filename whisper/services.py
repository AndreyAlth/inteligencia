import psycopg2
from config import load_config
# import json

def create_queue():
    """ create queue into queue table """

    sql = """
        insert into tasks (status) values('pending') returning *;
        """
    
    config  = load_config()
    id = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
                print(rows)
                if rows:
                    id = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    finally:
        return id
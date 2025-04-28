import psycopg2
from config import load_config
import json

def insert_transcription(id: str, data):
    """ Insert transcription into queue table """
    json_data = json.dumps(data)

    sql = """
        update tasks set data = %s, status= 'succeeded' where id = %s returning *;
        """
    
    config  = load_config()
    result = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (json_data, id))
                rows = cur.fetchall()
                if rows:
                    result = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return result

def update_transcription(id: str, data):
    """ Insert transcription into queue table """
    json_data = json.dumps(data)

    sql = """
        update tasks set data = %s where id = %s returning *;
        """
    
    config  = load_config()
    result = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (json_data, id))
                rows = cur.fetchall()
                if rows:
                    result = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return result

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
                if rows:
                    id = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    finally:
        return id

def get_queue(id: str):
    """ Retrieve data from the queue table """

    sql = """
        select * from tasks where id = %s
        """
    
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (id,))
                rows = cur.fetchall()
                return rows[0]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
def error_queue(queue_id):
    """ error queue into queue table """

    sql = """
        update tasks set status = 'failed' where id = %s returning *;
        """
    
    config  = load_config()
    id = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (queue_id))
                rows = cur.fetchall()
                if rows:
                    id = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    finally:
        return id


if __name__ == '__main__':
    pass
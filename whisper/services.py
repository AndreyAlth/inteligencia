import psycopg2
from config import load_config
import json

def insert_transcription(id: str, data):
    """ Insert transcription into queue table """
    print(data)
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
                    print(result)
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
                print(rows)
                if rows:
                    id = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    finally:
        return id
    
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
                print(rows)
                if rows:
                    id = rows[0]
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    finally:
        return id


if __name__ == '__main__':
    pass
import sqlite3
import uuid
from tango_driver import logger, config

'''
Handle buffer table
'''

def add_question(context, question):
    conn = sqlite3.connect(config.SQLITE_DB)
    cur = conn.cursor()

    new_req_id = str(uuid.uuid4())
    cur.execute('''INSERT INTO buffer 
                    (req_id, context, question, answer, answer_found)
                    VALUES (?,?,?,?,?)
                ''', (new_req_id,context,question," ",0))

    conn.commit()
            
    conn.close()   

    return new_req_id 


def add_answer(req_id, answer):

    conn = sqlite3.connect(config.SQLITE_DB)
    cur = conn.cursor()

    cur.execute(''' UPDATE buffer 
                    SET answer = ?, answer_found = 1
                    WHERE req_id = ?
                ''', (answer, req_id))

    conn.commit()
            
    conn.close()   

def get_answer(req_id):
    conn = sqlite3.connect(config.SQLITE_DB)
    cur = conn.cursor()

    cur.execute("SELECT answer, answer_found FROM buffer WHERE req_id = ? ", (req_id,))

    row = cur.fetchone()

    answer = "Answer Not Found"
    if row:
        found = row[1]
        if found :
            answer = row[0]
            
    conn.close()
    return answer

def get_new_question():
    conn = sqlite3.connect(config.SQLITE_DB)
    cur = conn.cursor()

    cur.execute("SELECT req_id, context, question FROM buffer WHERE answer_found = 0 ")

    row = cur.fetchone()

    new_question = None
    if row:
        new_question = {"req_id": row[0],
                        "context" : row[1],
                        "question" : row[2]}
            
    conn.close()
    return new_question
import os
import threading
import time
from tango_driver import logger
from tango_driver.utils import buffer_utils, answer_util

def daemon_process():
    logger.info("Daemon has started")
    while(True):
        try:
            new_rec = buffer_utils.get_new_question()
            if new_rec:
                logger.info("Trying to answer %s  %s", new_rec["req_id"] , new_rec["question"])
                answer = answer_util.get_answer(context=new_rec["context"], 
                                                question=new_rec["question"])

                buffer_utils.add_answer(req_id=new_rec["req_id"], answer=answer)
                logger.info("Got the answer %s %s", new_rec["req_id"], answer)
            
            time.sleep(1)

        except Exception as ex:
            logger.excetion("Error in daemon process")



    logger.info("Daemon has stopped")


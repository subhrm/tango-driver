from tango_driver import logger, config
import os

def get_context(topic):
    file_name = topic.lower().replace(" ","_")+".txt"
    dir_name = config.DATA_DIR

    text = ""

    with open(os.path.join(dir_name, file_name)) as fin:
        text = fin.read()

    return text

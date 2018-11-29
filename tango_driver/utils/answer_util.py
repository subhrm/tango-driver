import requests
import json
# from bs4 import BeautifulSoup

from tango_driver import config, logger

'''
    Get answer from model
'''

url = config.MODEL_URL


def get_answer(context, question):
    payload = {
        "passage": context,
        "question": question,
    }

    resp = requests.post(url, json=payload)

    logger.info(resp.status_code)

    if resp.status_code != config.HTTP_STATUS_OK:
        return {"answer": "An error occured.", "score": -2.0}

    return resp.json()

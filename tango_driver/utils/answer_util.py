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

    logger.info(payload)
    logger.info(resp.text)

    if resp.status_code != config.HTTP_STATUS_OK:
        return "An error occured."

    # soup = BeautifulSoup(resp.text, "html.parser")

    # answer = ""
    # try:
    #     answer = soup.find_all("span")[1].text
    # except Exception as ex:
    #     logger.exception("Some Error occured")
    #     answer = "An error occured"

    return resp.json()["answer"]

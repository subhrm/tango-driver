import requests
import json
import arrow
# from bs4 import BeautifulSoup

from tango_driver import config, logger

'''
    Apply leave 
'''

url = config.LMS_URL + "/applyleave"


def apply_leave(emp_id, st_date, end_date):

    date_1 = arrow.get(st_date, 'YYYY-MM-DD')
    date_2 = arrow.get(end_date, 'YYYY-MM-DD')

    diff = date_2 - date_1
    num_days = diff.days

    payload = {"emp_id": emp_id,
               "duration": num_days,
               "satrt_date": st_date,
               "end_date": end_date}
    resp = requests.post(url, json=payload)

    logger.info(resp.status_code)

    if resp.status_code != config.HTTP_STATUS_OK:
        logger.error("An error occured. Satus code %s", str(resp.status_code))
        return 0

    return num_days

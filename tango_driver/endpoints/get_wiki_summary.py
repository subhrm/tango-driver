
from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import buffer_utils

import wikipediaapi


@app.route('/api/get-wiki-summary/<topic>', methods=['get'])
def get_wiki_summary(topic):

    answer = "I am sorry. I faced an Internal error."

    try:
        wiki_en = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        wiki_page = wiki_en.page(topic)
        answer = wiki_page.text[:2000]

    except Exception as ex:
        logger.exception("Something went wrong")

    resp = make_response(json.dumps({"answer": answer}), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp

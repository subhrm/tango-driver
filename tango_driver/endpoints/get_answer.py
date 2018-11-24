
from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import buffer_utils


@app.route('/api/get-answer/<req_id>', methods=['get'])
def get_answer(req_id):
    
    answer = "I am sorry. I faced an Internal error."

    try:
        # Get POST parameters
        answer = buffer_utils.get_answer(req_id)

    except Exception as ex:
        logger.exception("Something went wrong")

    resp = make_response(json.dumps({"answer":answer}), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp
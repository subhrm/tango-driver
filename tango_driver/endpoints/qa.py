
from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import answer_util


@app.route('/api/qa', methods=['post'])
def do_qa():
    logger.info("Processing request for qa, verb: %s", str(request.method))

    if(request.headers['Content-Type'] != 'application/json'):
            return make_response('{"error":"unsupported content type"}', config.HTTP_STATUS_ERROR)

    logger.info(request.headers['Content-Type'])
    logger.info(request.get_data())
    # Get POST parameters
    input_json = request.json
    logger.info("Payload %s", json.dumps(input_json))

    context = input_json["context"]
    question = input_json["question"]

    answer = answer_util.get_answer(context, question)

    resp = make_response(json.dumps({"answer":answer}), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp
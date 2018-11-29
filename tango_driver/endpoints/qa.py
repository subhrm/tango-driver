
from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import answer_util, gk


@app.route('/api/qa', methods=['post'])
def do_qa():
    logger.info("Processing request for qa, verb: %s", str(request.method))
    answer = "I am sorry. I faced an Internal error."

    try:
        if(request.headers['Content-Type'] != 'application/json'):
            return make_response('{"error":"unsupported content type"}', config.HTTP_STATUS_ERROR)

        # Get POST parameters
        input_json = request.json

        context = input_json["context"]
        question = input_json["question"]
        context_type = int(input_json["type"])

        if context_type == 2:
            context = gk.get_context(context.strip())

        answer = answer_util.get_answer(context, question)
    except Exception as ex:
        logger.exception("Something went wrong")

    resp = make_response(json.dumps({"answer": answer}), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp

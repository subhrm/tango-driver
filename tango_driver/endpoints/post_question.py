
from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import buffer_utils, gk


@app.route('/api/post-question', methods=['post'])
def post_question():
    logger.info("Processing request for qa, verb: %s", str(request.method))
    req_id = ""

    try:
        if(request.headers['Content-Type'] != 'application/json'):
                return make_response('{"error":"unsupported content type"}', config.HTTP_STATUS_ERROR)

        logger.info(request.headers['Content-Type'])
        # Get POST parameters
        input_json = request.json

        context = input_json["context"]
        question = input_json["question"]
        context_type = int(input_json["type"])

        if context_type == 2:
            context = gk.get_context(context.strip())

        req_id = buffer_utils.add_question(context, question)
    except Exception as ex:
        logger.exception("Something went wrong")

    resp = make_response(json.dumps({"request_id":req_id}), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp

from flask import request, make_response, json
from tango_driver import app, logger, config
from tango_driver.utils import answer_util, intent_parser, lms_util


@app.route('/api/lms_driver', methods=['post'])
def do_lms_transaction():
    logger.info("Processing request for lams_driver, verb: %s",
                str(request.method))
    answer = {"answer": "I am sorry. I faced an Internal error.", "score": -2.0}

    try:
        if(request.headers['Content-Type'] != 'application/json'):
            return make_response('{"error":"unsupported content type"}', config.HTTP_STATUS_ERROR)

        # Get POST parameters
        input_json = request.json

        context = input_json["context"]
        question = input_json["question"]
        userObj = input_json["userObj"]

        intent_type, start_dt, end_dt = intent_parser.get_intent(question)

        logger.info("Queston : %s . intent:%s , dt1: %s, dt2: %s")

        if "apply_leave" in intent_type:
            num_days = lms_util.apply_leave(
                emp_id=userObj["employee_detail"]["emp_id"], st_date=start_dt, end_date=end_dt)

            answer = {"answer": "Leave applied for {} days".format(
                num_days), "score": 1.0, "userObj": userObj}
        else:
            answer = answer_util.get_answer(context, question)
            answer["userObj"] = userObj

    except Exception as ex:
        logger.exception("Something went wrong")

    resp = make_response(json.dumps(answer), config.HTTP_STATUS_OK)
    resp.headers['Content-Type'] = 'application/json'

    return resp

import json
import os
import sys
from datetime import datetime, timedelta

import spacy
from rasa_nlu.model import Interpreter

from tango_driver import config, logger

nlp = spacy.load("en")

intent_interpreter = Interpreter.load(
    config.RASA_MODEL_DIR + "/intent_models/current/intent_nlu")
date_interpreter = Interpreter.load(
    config.RASA_MODEL_DIR + "/date_models/current/date_nlu")


def get_intent(message):
    result = intent_interpreter.parse(message)
    #print(json.dumps(result, indent=2))
    # print(result['intent']['name'])
    intent = result['intent']['name']

    startDate = ''
    endDate = ''

    if "apply_leave" in intent:
        txt = nlp(message)
        for word in txt.ents:
            print(word.text, word.label_)
            result1 = date_interpreter.parse(word.text)
            if len(result1['entities']) > 2:
                startDate = result1['entities'][1]['value']['from'].split('T')[
                    0]
                endDate = result1['entities'][1]['value']['to'].split('T')[0]
            else:
                startDate = result1['entities'][0]['value'].split('T')[0]
                endDate = result1['entities'][0]['value'].split('T')[0]

    return (intent, startDate, endDate)

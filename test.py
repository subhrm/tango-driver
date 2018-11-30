from time import time
t0 = time()

from tango_driver.utils import intent_parser

print("Time taken for loading {} secs".format(time()-t0))

t0 = time()

print(intent_parser.get_intent("Apply leave for next two days"))
print("Time taken = {} secs".format(time()-t0))
print(intent_parser.get_intent("Apply leave for next three days"))
print("Time taken = {} secs".format(time()-t0))
print(intent_parser.get_intent("Apply leave for next four days"))
print("Time taken = {} secs".format(time()-t0))

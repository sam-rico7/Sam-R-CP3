import logging

logging.basicConfig(level=logging.DEBUG)

def buggy_function(a, b):
    result = a * b
    logging.debug(f"a: {a} b: {b} result: {result}")
    return result

#we could use an assert here
print(buggy_function("2", 3)) #Expected output: 6
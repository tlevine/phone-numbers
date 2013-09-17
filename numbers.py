from collections import defaultdict
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def response_factory():
    responses = defaultdict(lambda: )
    responses[0][''] = mc.DiscreteUniform('_', 0, 9)
    return responses

def add(responses, phone_number):
    for i in range(1, len(phone_number) - 1):
        if phone_number[:i] not in responses[i]:
            responses[i][phone_number[:i]] = mc.DiscreteUniform('_' + phone_number[:i], 0, 9)
    return responses

def select(responses):
    n = 13
    phone_number = ''
    for i in range(0, n):
        digit = responses[i][phone_number].random()
        phone_number += str(digit)
    return phone_number

responses = response_factory()
for pn in phone_numbers:
    responses = add(responses, pn)
print select(responses)

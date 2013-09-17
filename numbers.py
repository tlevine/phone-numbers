from collections import defaultdict
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def _digit_distribution():
    return mc.DiscreteUniform('d' + phone_number[:i], 0, 9)

def responses_factory():
    return defaultdict(lambda: defaultdict(_digit_distribution))

def add(responses, phone_number):
    for i in range(1, len(phone_number) - 1):
        responses[i][phone_number[:i]]
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

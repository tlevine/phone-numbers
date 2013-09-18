from collections import defaultdict, Counter
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def response_factory():
    return defaultdict(Counter)

def add(responses, phone_number):
    for i in range(0, len(phone_number) - 1):
        responses[phone_number[:i]].update([int(phone_number[i])])
    return responses

def ml_estimate(counter):
    s = 0.0 + sum(counter.values())
    return [(counter[digit] + 0.0)/s for digit in range(0,10)]

responses = response_factory()
for pn in phone_numbers:
    responses = add(responses, pn)
print responses['880129243']

d = {}
for key in responses.keys():
    print key
    d[key] = mc.Categorical('_' + key, ml_estimate(responses[key]))

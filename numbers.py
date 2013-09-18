from collections import defaultdict, Counter
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def digit_distribution(values):
    return mc.Categorical('d', values)

def response_factory():
    return defaultdict(lambda: defaultdict(Counter))

def add(responses, phone_number):
    for i in range(0, len(phone_number) - 1):
        next_digit = int(phone_number[i + 1])
        responses[i][phone_number[:i]].update([next_digit])
    return responses

responses = response_factory()
for pn in phone_numbers:
    responses = add(responses, pn)
print responses[3]['880']

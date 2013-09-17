from collections import defaultdict
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def train(belief, phone_number):
    for pn in partials(phone_number):
        if pn not in belief:
            belief[pn] = mc.DiscreteUniform('_' + pn, 0, 9)

    return belief

def partials(phone_number):
    out = set()
    for i in range(0, len(phone_number)):
        out.add(phone_number[:i])
    return out

pns = partial_numbers(phone_numbers)
distributions = {pn:  for pn in pns}

def

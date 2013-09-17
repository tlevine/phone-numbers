import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def partial_numbers(phone_numbers):
    out = set()
    for phone_number in phone_numbers:
        for i in range(0, len(phone_number)):
            out.add(phone_number[:i])
    return out

pns = partial_numbers(phone_numbers)
distributions = {pn: mc.DiscreteUniform(pn, 0, 9) for pn in pns}

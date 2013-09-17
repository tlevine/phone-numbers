'''Let's do this with a normal approximation.'''
from collections import Counter
phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

class PhoneCounter(Counter):
    def prefixed(self, prefix):
        'Phone numbers with a prefix'
        return filter(lambda key: key.startswith(prefix), self.keys())

    def prefixes(self, phone_number):
        'Prefixes of a phone number'
        keys = filter(lambda key: phone_number.startswith(key), self.keys())


def branch(subbranch,

def count_factory():
    return (0, defaultdict(count_factory))

def partial_numbers(phone_number, end = None):
    if end == None:
        end = len(phone_number)
    return [phone_number[-i:] for i in range(1, end)]

def add(counts, phone_number):
    for i in range(0, len(phone_number)):
        for p in partial_numbers(phone_number, i):
            counts[p][0] += 1
            counts[p][1] += 1

    return counts

def predict(counts, phone_number):
    partial_numbers(phone_number)

'''Let's do this with a normal approximation.'''
from collections import Counter

class PhoneCounter(Counter):
    def prefixed(self, prefix):
        'Phone numbers with a prefix'
        return filter(lambda key: key.startswith(prefix), self.keys())

    def prefixes(self, phone_number):
        'Prefixes of a phone number'
        return filter(lambda key: phone_number.startswith(key), self.keys())

    def next_prefixes(self, prefix):
        return filter(lambda key: key[:-1] == prefix, self.keys())

    def add(self, phone_number):
        for i in range(1, len(phone_number)):
            self.update([phone_number[:i]])

def sort(strings):
    return sorted(strings, cmp = _cmp_len)

def _cmp_len(a,b):
    la = len(a)
    lb = len(b)
    if la > lb:
        return 1
    elif la < lb:
        return -1
    else:
        return 0

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]
c = PhoneCounter()
for phone_number in phone_numbers:
    c.add(phone_number)

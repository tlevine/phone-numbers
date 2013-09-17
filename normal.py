'''Let's do this with a normal approximation.'''
class PhoneCounter(set):
    def prefixed(self, prefix):
        'Phone numbers with a prefix'
        return filter(lambda key: key.startswith(prefix), self)

    def prefixes(self, phone_number):
        'Prefixes of a phone number'
        return filter(lambda key: phone_number.startswith(key), self)

    def next_prefixes(self, prefix):
        return filter(lambda key: key[:-1] == prefix, self)

    def counts(self, prefix = ''):
        return {p:len(self.prefixed(p)) for p in self.next_prefixes(prefix)}

    def random(self, prefix = '')

    def add_phone_number(self, phone_number):
        for i in range(1, len(phone_number)):
            self.add(phone_number[:i])

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
    c.add_phone_number(phone_number)

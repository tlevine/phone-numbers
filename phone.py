from collections import defaultdict, Counter, OrderedDict
from random import uniform

def categoricalvariate(w, x = None):
    '''
    Args:
        values: A dictionary mapping keys to weights, where weights sum to one.
    Returns:
        One of the keys, chosen randomly

    >>> categoricalvariate(OrderedDict([('0', 0.3), ('1', 0.6), ('2', 0.1)]), x = 0.98)
    '2'

    >>> categoricalvariate(OrderedDict([('0', 0.3), ('1', 0.6), ('2', 0.1)]), x = 0.1)
    '0'

    >>> categoricalvariate(OrderedDict([('0', 0.3), ('1', 0.6), ('2', 0.1)]), x = 0.5)
    '1'
    '''
    if x == None:
        x = uniform(0, 1)

    cdf = reduce(lambda a, b: a + [a[-1] + b], w.values()[1:], [w.values()[0]])
    for _k, _cdf in zip(w.keys(), cdf):
        if x < _cdf:
            return _k

def observations_factory():
    return defaultdict(Counter)

def observe_phone_number(observations, number):
    'Add the phone number stuff to the observations dict.'
    for i in range(len(number)):
        observations[number[:i]].update(number[i])
    return observations

def smooth(counter, keys = '0123456789'):
    '''
    Apply +1 smoothing to a counter.

    Args:
        counter: The counter to be smoothed
        keys: The keys that are allowed to have values
    Returns:
        A smoothed counter, with one added to each value

    >>> smooth(Counter('bcb'), keys = 'abcde')
    Counter({'b': 3, 'c': 2, 'a': 1, 'e': 1, 'd': 1})

    '''
    smoothed_counter = Counter(counter)
    smoothed_counter.update(keys)
    return smoothed_counter

def weight(counter):
    '''
    Turn counts into weights.

    Args:
        counter: A dictionary to be weighted
    Returns:
        A dictionary mapping keys to weights, where weights sum to one.

    >>> weight({'a': 8, 'b': 2})
    {'a': 0.8, 'b': 0.2}
    '''
    s = float(sum(counter.values()))
    return {k: float(v)/s for k, v in counter.items()}


def choose_next_digit(observations, partial_number):
    w = weight(smooth(observations[partial_number]))
    return categoricalvariate(w)

def is_valid(phone_number):
    '''
    Check whether a phone number is valid.

    Args:
        phone_number: A phone number to be validated
    Returns:
        True or False

    Phone numbers must be 13 characters long.

    >>> is_valid('12120000000')
    False

    >>> is_valid('0012120000000')
    True

    Phone numbers that are shorter than 13 characters should
    be padded with spaces on the right.

    >>> is_valid('88011111111  ')
    True

    >>> is_valid('  88011111111')
    False

    Phone numbers must be string-like.

    >>> is_valid([0, 0, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0])
    False

    Phone numbers may only contain the characters [0-9]

    >>> is_valid('001212000000b')
    False

    '''
    try:
        '' + phone_number
    except:
        return False

    return len(phone_number) == 13 and all(map(lambda x: x in '0123456789', phone_number.rstrip(' ')))

def load_phone_numbers(filename_or_list):
    if hasattr(filename_or_list, '__len__'):
        return filename_or_list
    return ['0' * 13, '8' * 13]

def generate_number(observations):
    number = choose_next_digit(observations, '')
    while len(number) < 13:
        number += choose_next_digit(observations, number)
    return number

import re
def pretty_print(phone_number):
    spaced = ' '.join([phone_number[:3], phone_number[3:6], phone_number[6:9], phone_number[9:13]])
    unpadded = re.sub(r'^0', ' ', re.sub(r'^00', r'  ', spaced))
    plus = re.sub(r'^( *)([0-9])', r'\1+\2', unpadded)
    return plus


def run(phone_numbers, how_many_new_numbers):
    o = observations_factory()
    for phone_number in phone_numbers:
        if not is_valid(phone_number):
            raise ValueError('"%s" is not a valid phone number.' % phone_number)

        o = observe_phone_number(o, phone_number)

    for i in range(how_many_new_numbers):
        print pretty_print(generate_number(o))

def from_file(filename):
    '''
    Args:
        filename: Name of a file containing phone numbers in the particular format
    Returns:
        Iterable of 13-character phone number strings
    '''
    fp = open(filename)
    fp.readline() # Burn the header
    for line in fp.readlines():
        number = line.rstrip()
        # Right-pad short phone numbers.
        # Consider doing this part differently.
        yield number + ' ' * (13 - len(number))

def test():
    import doctest
    doctest.testmod()

def main():
    import sys

    if len(sys.argv) == 1:
        filename = 'BG_10K_12.csv'
        how_many_new_numbers = 7
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        how_many_new_numbers = int(sys.argv[2])
    else:
        print 'USAGE: %s [[phone numbers file] [how many numbers to generate]]' % sys.argv[0]
        exit(1)

    run(from_file(filename), how_many_new_numbers)

if __name__ == '__main__':
    test()
    # main()

from collections import defaultdict, Counter

import pymc

def observations_factory():
    return defaultdict(Counter)

def observe_phone_number(observations, number):
    'Add the phone number stuff to the observations dict.'
    for i in range(len(number)):
        observations[number[:i]].update(number[i])
    return observations

def smooth(counter, keys = map(str, range(10))):
    '''
    Apply +1 smoothing to a counter.

    >>> smooth(Counter('bcb'), 'abcde')
    Counter('abcdebcb')

    '''
    smoothed_counter = Counter(counter)
    smoothed_counter.update(smoothed_counter.keys()
    return smoothed_counter

def weight(counts):
    'Turn counts into weights.'

def choose_next_digit(observations, partial_number):
    weights = smooth(observations[partial_number])
    pymc.Categorical

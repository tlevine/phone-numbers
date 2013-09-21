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
    weights = smooth(observations[partial_number])
    pymc.Categorical

if __name__ == '__main__':
    import doctest
    doctest.testmod()

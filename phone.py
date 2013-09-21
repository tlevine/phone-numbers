from collections import defaultdict, Counter

import pymc

def observations_factory():
    return defaultdict(Counter)

def observe_phone_number(observations, number):
    'Add the phone number stuff to the observations dict.'
    for i in range(len(number)):
        observations[number[:i]].update(number[i])
    return observations

def phone_digit(observations):
    pymc.Categorical

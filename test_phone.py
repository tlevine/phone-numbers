import nose.tools as n

import phone

def test_observations_factory():
    n.assert_dict_equal(phone.observations_factory(), {})

def test_observe_phone_number():
    o = phone.observations_factory()
    o = phone.observe_phone_number(o, '1212' + '123456')
    o = phone.observe_phone_number(o, '1212' + '123488')
    e = {
        '': {'1': 2}, '1212': {'1': 2}, '12': {'1': 2},
        '1': {'2': 2}, '121': {'2': 2}, '121212': {'3': 2},
        '12121': {'2': 2}, '1212123': {'4': 2},
        '12121234': {'5': 1, '8': 1},
        '121212345': {'6': 1},
        '121212348': {'8': 1},
    }
    n.assert_dict_equal(o, e)

def test_smooth():
    o = phone.smooth(Counter('bcb'), keys = 'abcde')
    e = Counter({'b': 3, 'c': 2, 'a': 1, 'e': 1, 'd': 1})
    n.assert_dict_equal(o, e)

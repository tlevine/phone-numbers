import nose.tools as n

import phone

def test_observations_factory():
    n.assert_dict_equal(phone.observations_factory(), {})

def test_observe_phone_number():
    o = phone.observations_factory()
    o = phone.observe_phone_number(o, '1212' + '123456')
    e = {
        '': {'1': 1}, '1212': {'1': 1}, '12': {'1': 1},
        '12121234': {'5': 1}, '1': {'2': 1}, '121': {'2': 1},
        '121212': {'3': 1}, '12121': {'2': 1},
        '1212123': {'4': 1}, '121212345': {'6': 1}
    }
    n.assert_dict_equal(o, e)

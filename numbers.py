from collections import defaultdict
import pymc as mc

phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

class Belief:
    def __init__(self):
        self.d = {}

    def add(self, phone_number):
        for i in range(1, len(phone_number) - 1):
            self.d[phone_number[:i]] = mc.DiscreteUniform('_' + pn, 0, 9)

    def select

    @mc.deterministic
    def lambda_(tau=tau, lambda_1=lambda_1, lambda_2=lambda_2):
        out = np.zeros(n_data_points)
        out[tau:] = lambda_2  # lambda after tau is lambda1
        return out"

def train(belief, phone_number):
    for pn in partials(phone_number):
        if pn not in belief:
            belief[pn] = mc.DiscreteUniform('_' + pn, 0, 9)

    return belief

def partials(phone_number):
    out = set()
    for i in range(0, len(phone_number)):
        out.add(phone_number[:i])
    return out

pns = partial_numbers(phone_numbers)
distributions = {pn:  for pn in pns}

def

'''Let's do this with a normal approximation.'''
phone_numbers = [
    '8801292432439',
    '8801292432694',
    '8801292432275',
    '8801292432437',
]

def partial_numbers(phone_number):
    return [phone_number[:i] for i in range(0, len(phone_number))]

def add(counts, phone_number):
    counts.update(partial_numbers(phone_number))
    return counts

def predict(counts, phone_number):
    partial_numbers(phone_number)

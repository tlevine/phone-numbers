Most phone numbers are not active, so we expect a
rather low response rate when we use random phone
numbers to sample people. This gets expensive.

To improve our response rate, we select numbers
based on historical responses. `phone.py` selects
new random numbers based on historically responsive
phone numbers.

This is how you generate 20 numbers based on the `BG_10K_12.csv` file.

    ./phone.py BG_10K_12.csv 20

## To do

1. Explain how it works
2. Make pretty visuals to see what the groupings are;
    local area codes and lucky numbers will pop out.
3. Consider whether short phone numbers should be handled differently.
4. Improve the smoothing algorithm
    Currently it's just +1 smoothing, and it doesn't handle short phone numbers.

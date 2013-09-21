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
In approximate order of priority

1. Explain how it works
2. Make pretty visuals to see what the groupings are;
    local area codes and lucky numbers will pop out.
3. Connect this to other information about the phone numbers so
    we can run fancy stratified samples. Possibilities include
  * how many times the number has been called
  * how many times the number has responded
  * which cell phone towers the calls came from
4. Consider whether short phone numbers should be handled differently.
5. Improve the smoothing algorithm
    Currently it's just +1 smoothing, and it doesn't handle short phone numbers.

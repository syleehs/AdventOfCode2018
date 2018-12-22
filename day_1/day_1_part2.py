input = open("input.txt", "r")
changes = [int(n) for n in input.split()]
from itertools import accumulate, cycle
seen = set()
print(next(f for f in accumulate(cycles(changes))
if f in seen or seen.add(f)))
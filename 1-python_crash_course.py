#%%
# defaultdicts
from collections import defaultdict

l = defaultdict(list)
l[2].append(1)
print(l)

# Counters
from collections import Counter

c = Counter([0, 0, 1, 1])
for i in c.elements():
    print(i)

# zip
l1 = list('abc')
l2 = [1, 2, 3]
l3 = [None, None, None]

a = [t for t in zip(l1, l2, l3)]

# type annotations
from typing import List
def total(xs: List[float]) -> float:
    return sum(xs)

values: List[int] = []
for i in range(10):
    values.append(i)

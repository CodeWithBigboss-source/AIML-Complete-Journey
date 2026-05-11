# this only works in jupyter notebook
# import numpy as np
# import timeit
# time = timeit.timeit( [item**3 for item in range(1,9)])
# t = timeit.timeit (np.arange(1,9)**3)

import numpy as np
import timeit

time = timeit.timeit(
    '[item**3 for item in range(1,9)]',
    number=100000
)

t = timeit.timeit(
    'np.arange(1,9)**3',
    number=100000,
    globals=globals()
)

print(time)
print(t)

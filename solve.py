# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)
    def fill_table():
        for i in range (1, len(items)+1):
            for w in range(1, capacity+1):
                if items[i-1].weight <= w:
                    if items[i-1].value + table[i-1, w-items[i-1].weight] > table[i-1, w]:
                        table[i, w] = items[i-1].value + table[i-1, w-items[i-1].weight]
                    else:
                        table[i, w] = table[i-1, w]
                else:
                    table[i, w] = table[i-1, w]
        return
    
    def fill_taken(n,w):
        i = n
        k = w

        while i > 0 and k > 0:
            if table[i,k] != table[i-1,k]:
                taken.append(items[i-1].index)
                i -= 1
                k -= items[i].weight
            else:
                i -= 1
        return

    n=len(items)
    w=capacity
    
    fill_table()                # Relleno la tabla

    fill_taken(n,w)             # Genero la lista de items elegidos

    return table[n,w], list(reversed(taken))
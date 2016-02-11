# input
x = '()((())'

# Mapping dict
M = {'(': 1, ')': -1}

# Solution
print sum([M.get(c) for c in x])
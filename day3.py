# input
#inp = '^>v<'
inp = '^v^v^v^v^v'

# Mapping dict
M = {
	'<': (-1, 0),
	'>': (1, 0),
	'^': (0, 1),
	'v': (0, -1)
}

visited = [] # list to store all visited coordinates

# start position
x, y = 0, 0
visited.append((x, y))

# update coordinates according to input pattern 
for p in inp:
	x, y = x + M.get(p)[0], y + M.get(p)[1]
	visited.append((x, y))

# set to get unique visited coordinates
print len(set(visited))
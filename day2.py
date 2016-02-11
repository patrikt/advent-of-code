# input
x = ['29x13x26', '11x11x14', '27x2x5']

# calculate square feet per dimension
def square_feet(dim):
	l, w, h = int(dim.split("x")[0]), int(dim.split("x")[1]), int(dim.split("x")[2])
	lw, wh, hl = l*w, w*h, h*l
	return min(lw, wh, hl) + 2 * (lw + wh + hl)

# Solution
print sum([square_feet(v) for v in x])

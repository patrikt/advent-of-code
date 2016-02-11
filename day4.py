import hashlib

inp = "yzbqklnj"

i = 1
s = inp + str(i) 
h = hashlib.md5(s).hexdigest()

while (h[0] == '0') & (h[1] == '0') & (h[2] == '0') & (h[3] == '0') & (h[4] == '0') == False:
	i = i + 1
	s = inp + str(i)
	h = hashlib.md5(s).hexdigest()

print i, s, h
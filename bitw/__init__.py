import numpy

def read_txt(file):
	data = dict()
	txt = open(file).read()
	def chread(x):
		if x in "0 .":
			return 0
		return 1
	for block in txt.split("\n\n"):
		lines = block.split("\n")
		if not lines[-1]: # new line in end of file
			lines = lines[:-1]
		unicode = int(lines[0])
		a = numpy.array(
			[list([chread(x) for x in line])
				for line in lines[1:]
			],
			dtype = numpy.uint8)
		data[unicode] = a
	h, w = data[32].shape
	return data, w, h

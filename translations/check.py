def read_seq(inputfile):
	"""Reads and returns the input sequence with special characters removed."""
	with open(inputfile, "r") as f:
		seq = f.read()
	seq = seq.replace("\n", "")
	seq = seq.replace("\r", "")
	return seq
import sys

def histogram(source_text):
	with open(source_text, 'r') as file:
		words = file.read().split()
	histogram = dict()
	for word in words:
		if word in histogram:
			histogram[word] += 1
		else:
			histogram[word] = 1
	return histogram

if __name__ == '__main__':
	source_text = sys.argv[1]
	print(histogram(source_text))
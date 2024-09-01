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

def unique_words(histogram):
	unique_words = []
	for key in histogram:
		if histogram[key] == 1:
			unique_words.append(key)
	return unique_words

if __name__ == '__main__':
	source_text = sys.argv[1]
	histogram = histogram(source_text)
	print('~-~-~-~-~-~-~-~-~ Histogram ~-~-~-~-~-~-~-~-~')
	print(histogram)
	unique = sys.argv[2:]
	if 'unique_words' in unique:
		print('\n~-~-~-~-~-~-~-~-~ Unique Words ~-~-~-~-~-~-~-~-~')
		print(unique_words(histogram))
		
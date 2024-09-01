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

def frequency(word, histogram):
	return histogram[word]

if __name__ == '__main__':
    source_text = sys.argv[1]
    unique_arg = sys.argv[2:]
    frequency_arg = sys.argv[3:]
    word_arg = sys.argv[4:]
    histogram_data = histogram(source_text)
    print('~-~-~-~-~-~-~-~-~ Histogram ~-~-~-~-~-~-~-~-~')
    print(histogram_data)
    if 'unique_words' in unique_arg:
        print('\n~-~-~-~-~-~-~-~-~ Unique Words ~-~-~-~-~-~-~-~-~')
        print(unique_words(histogram_data))
    if 'frequency:' in frequency_arg:
        print('\n~-~-~-~-~-~-~-~-~ Frequency of Word ~-~-~-~-~-~-~-~-~')
        print(frequency(word_arg[0], histogram_data))
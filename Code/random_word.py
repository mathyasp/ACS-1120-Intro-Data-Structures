import time
import sys
from histogram import histogram

def random_number():
    return int(time.time() * 1000) % 100000

def random_word(histogram):
    words = list(histogram.keys())
    rand_num = random_number()
    valid_words = [word for word in words if word.isalpha()]
    weights = [histogram[word] for word in valid_words]
    total = sum(weights)
    rand_num = rand_num % total
    for i, weight in enumerate(weights):
        rand_num -= weight
        if rand_num <= 0:
            return valid_words[i]

if __name__ == '__main__':
    source_text = sys.argv[1]
    histogram_data = histogram(source_text)
    print('~-~-~-~-~-~-~-~-~ Random Word ~-~-~-~-~-~-~-~-~')
    print(random_word(histogram_data))
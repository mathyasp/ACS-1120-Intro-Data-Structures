import sys

def reverse_words(words):
    return ' '.join([word[::-1] for word in words])

if __name__ == '__main__':
    words = sys.argv[1:]
    print(reverse_words(words))
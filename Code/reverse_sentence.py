import sys

def reverse_sentence(words):
    return ' '.join(words[::-1])

if __name__ == '__main__':
    words = sys.argv[1:]
    print(reverse_sentence(words))
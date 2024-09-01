import sys

def anagram_generator(word):
    with open('/usr/share/dict/words') as file:
        words = file.read().split()
        anagrams = [w for w in words if sorted(w) == sorted(word)]
        return anagrams

if __name__ == '__main__':
    word = sys.argv[1]
    print(anagram_generator(word))
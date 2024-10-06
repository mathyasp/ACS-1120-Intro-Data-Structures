from dictogram import Dictogram
import random

class MarkovChain:
    """TODO: Learn a Markov chain from a corpus. You’ve already written code to find how often a token appears in a corpus, but now you need to find how often a token appears after another token.
    Do a random walk on a Markov chain. This should be pretty simple if you pick a good way to store the Markov chain you learn."""
    
    def __init__(self, word_list=None):
        """Initialize this Markov chain as a new dictionary and count given words."""
        self.states = Dictogram()
        self.word_list = word_list if word_list is not None else []
        self.types = 0
        self.tokens = 0
        if self.word_list:
            self.markov_chain()
    
    def markov_chain(self):
        """Create a Markov chain from the given list of words."""
        for i in range(len(self.word_list) - 1):
            if self.states.__contains__(self.word_list[i]):
                self.states[self.word_list[i]].add_count(self.word_list[i + 1])
            else:
                self.states[self.word_list[i]] = Dictogram([self.word_list[i + 1]])
                self.types += 1
            self.tokens += 1
    
    def sample(self, word):
        """Return a word from this Markov chain, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        if word in self.states:
            return self.states[word].sample()
        return None
    
    def generate_sentence(self, length=10):
        """Generate a sentence from this Markov chain of the given length."""
        sentence = []
        word = random.choice(self.word_list)
        for _ in range(length):
            sentence.append(word)
            word = self.sample(word)
            if word is None:
                word = random.choice(self.word_list)
        return ' '.join(sentence)
    
    def print_markov_chain(self, word_list):
        print()
        print('Markov Chain:')
        print('word list: {}'.format(word_list))
        # Create a Markov chain and display its contents
        markov_chain = MarkovChain(word_list)
        print('markov chain: {}'.format(markov_chain))
        print('{} tokens, {} types'.format(markov_chain.tokens, markov_chain.types))
        for word in word_list[-2:]:
            next_word = markov_chain.sample(word)
            print('{!r} -> {!r}'.format(word, next_word))
        print()
        self.print_markov_chain_samples(markov_chain)
    
    def print_markov_chain_samples(self, markov_chain):
        print('Markov Chain samples:')
        # Sample the Markov chain 10,000 times and count frequency of results
        samples_list = [markov_chain.generate_sentence() for _ in range(10000)]
        samples_hist = Dictogram(samples_list)
        print('samples: {}'.format(samples_hist))
        print()

def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    markov_chain = MarkovChain()
    if len(arguments) >= 1:
        # Read the file contents
        file_path = arguments[0]
        with open(file_path, 'r') as file:
            text = file.read()
        # Split the text into words
        word_list = text.split()
        # Create a Markov chain and generate a sentence
        markov_chain = MarkovChain(word_list)
        sentence = markov_chain.generate_sentence()
        print(sentence)
    else:
        # Test the Markov chain on a simple example
        word_list = ['I', 'am', 'a', 'robot', 'sent', 'from', 'the', 'future']
        markov_chain = MarkovChain(word_list)
        sentence = markov_chain.generate_sentence()
        print(sentence)

if __name__ == '__main__':
    main()
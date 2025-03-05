import random
from dictogram import Dictogram


class MarkovChain(dict):
    def __init__(self, corpus):
        # Turn the input text into a list of words if it's a string
        if isinstance(corpus, str):
            self.corpus = corpus.split()
        else:
            self.corpus = corpus

        for i in range(len(self.corpus) - 1):
            current_word = self.corpus[i]
            next_word = self.corpus[i + 1]

            if current_word not in self:
              new_histogram = Dictogram([next_word])
              self[current_word] = new_histogram
            else:
              histogram = self[current_word]
              histogram.add_count(next_word)

    def walk(self, length=10):
        # Start with a random word
        current_word = random.choice(list(self.keys()))
        words = [current_word]

        # Generate next words
        for _ in range(length-1):
            if current_word not in self:
                break
            current_word = self[current_word].sample()
            words.append(current_word)

        return ' '.join(words)


if __name__ == '__main__':
    text = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
    chain = MarkovChain(text)

    print("Markov Chain contents:")
    for word in chain:
        print(f"{word}: {dict(chain[word])}")

    print("\nGenerated sentences:")
    for _ in range(3):
        print(chain.walk())

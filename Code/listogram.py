#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # Check if word already exists in histogram
        found = False
        i = 0
        while i < len(self):
            word_in_list = self[i][0]
            count_in_list = self[i][1]

            # If we found the word
            if word_in_list == word:
                new_count = count_in_list + count
                self[i] = [word, new_count]
                self.tokens = self.tokens + count
                found = True
                break
            i = i + 1

        # If we didn't find the word, add it as new
        if not found:
            self.append([word, count])
            self.types = self.types + 1
            self.tokens = self.tokens + count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        i = 0
        while i < len(self):
            current_word = self[i][0]
            current_count = self[i][1]

            if current_word == word:
                return current_count
            i = i + 1

        # If we didn't find the word, return 0
        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        i = 0
        while i < len(self):
            current_word = self[i][0]
            if current_word == word:
                return True
            i = i + 1
        return False

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        i = 0
        while i < len(self):
            current_word = self[i][0]
            if current_word == target:
                return i
            i = i + 1

        return None

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        # First get the total number of all words
        total_words = 0

        for item in self:
            word_count = item[1]
            total_words = total_words + word_count

        random_pick = random.uniform(0, total_words)

        # Go through each word
        running_total = 0
        for item in self:
            word = item[0]
            count = item[1]
            running_total = running_total + count

            if running_total >= random_pick:
                return word


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(
            error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()

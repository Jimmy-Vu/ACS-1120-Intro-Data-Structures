import sys
import re

def histogram(source_text):
    with open(source_text, "r") as file:
        text = file.read().lower()
        words = re.split(r"\W+", text)
        word_frequency = {}
        for word in words:
            if word:
                word_frequency[word] = word_frequency.get(word, 0) + 1

    # print("Histogram:", word_freq)
    return word_frequency


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word, 0)


if __name__ == "__main__":
    filename = sys.argv[1]
    hist = histogram(filename)

    print(f"Unique words: {unique_words(hist)}")

    word = "the"
    print(f"Frequency of '{word}': {frequency(word, hist)}")

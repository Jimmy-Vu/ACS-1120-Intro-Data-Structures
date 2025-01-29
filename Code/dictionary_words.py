import sys
import random

words_file = "/usr/share/dict/words"

def create_sentence(word_count):
  with open(words_file, "r") as file:
      words = [line.strip() for line in file.readlines()]
  chosen_words = random.sample(words, word_count)
  print(" ".join(chosen_words))

if __name__ == "__main__":
   word_count = int(sys.argv[1])
   create_sentence(word_count)

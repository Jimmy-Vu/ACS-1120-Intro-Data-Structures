import random
import sys
random.seed()

def rearrange(words):
  random.shuffle(words)
  return " ".join(words)


words = sys.argv[1:]
rearranged_words = rearrange(words)
print(rearranged_words)

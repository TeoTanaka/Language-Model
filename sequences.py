from preprocess import text
from preprocess import wordlist
from preprocess import text_nums
from preprocess import text_to_num
from preprocess import num_to_text
LEN_SEQUENCE = 25
sequences = []
targets = []

for i in range(len(text)-LEN_SEQUENCE):
    sequences.append(text[i:i+25])
    targets.append(text[i+25])

#for i in range(len(sequences)):
       #print(f"{sequences[i]} :: {targets[i]}")


num_sequences = []
num_targets = []

for a in sequences:
      num_sequences.append(text_to_num(wordlist,[a]))
for b in targets:
      num_targets.append(text_to_num(wordlist,[b]))

for i in range(len(num_sequences)):
    pass
    #    print(f"{num_sequences[i]} :: {num_targets[i]}")
      
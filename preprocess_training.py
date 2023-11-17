
vocab = []
with open("words.txt") as file:#the convergion words
    vocab = list(file)

raw_training = []
with open("training.txt") as file:#the convergion words
    raw_training = list(file)
#Convering training data to letters
token_input=[]
def tokenize(input,vocab):
  token_input = []
  for a in input:
      if a in vocab:
          token_input.append(vocab.index(a))
      else:
        print("error on word", a)
        vocab.append(a)
        token_input.append(vocab.index(a))
  return token_input, vocab

tokens, new_vocab = tokenize(raw_training,vocab)





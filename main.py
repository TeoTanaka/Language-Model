import numpy as np
from preprocess import text
from preprocess import wordlist
from preprocess import text_nums
from preprocess import text_to_num
from preprocess import num_to_text
from sequences import num_sequences
from sequences import num_targets
# Print(text_to_num(wordlist,["I"]))
# Print(num_to_text(text_nums,wordlist,[12]))


# Generating randomized archetecture for RNN
VOCAB_SIZE = len(text)
HIDDEN_SIZE = 130
LEARNING_RATE = .01

# Defining weights w=weight, I = input layer, H = hidden layer, O = output layer, b = bias
wI_H = np.random.randn(HIDDEN_SIZE, 1) * LEARNING_RATE
wH_H = np.random.randn(HIDDEN_SIZE, 1) * LEARNING_RATE
wH_O = np.random.randn(HIDDEN_SIZE, 1) * LEARNING_RATE

bH = np.zeros((HIDDEN_SIZE, 1))
bO = np.zeros((HIDDEN_SIZE, 1))

# Forward pass
def forward_pass(num_sequences,num_targets):
    outputs = {}
    hiddens = {}
    hiddens[-1] = 0
    loss  = 0
    for a in range(len(num_targets)):
        hiddens[a] = np.tanh(np.dot(wI_H, num_sequences[a])+ np.dot(wH_H, hiddens[a-1]) + bH)  #forward pass algorithms # Got this algorithm from chatGPT
        hiddens[a] = np.tanh(np.dot(wH_H, num_sequences[a])+ np.dot(wI_H, hiddens[a]) + bO)
    print(hiddens)

forward_pass(num_sequences, num_targets)

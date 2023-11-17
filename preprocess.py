#https://www.kaggle.com/datasets/Cornell-University/movie-dialog-corpus
from typing import List
import numpy as np

#OPENING FILE HELP FROM CHATGPT
def tokenize(file_path: str) -> List[str]:
    tokens = []
    with open(file_path,'r') as file:
        for line in file:
            for word in line.split():
                if not "." in word and not "," in word and not "!" in word and not "?" in word and not ";" in word and not ":" in word:#else at bottom was repeating characters
                    tokens.append(word)
                
                if "." in word:
                    word = word[:word.find(".")]
                    tokens.append(word)
                    tokens.append(".")
                if "!" in word:
                    word = word[:word.find("!")]
                    tokens.append(word)
                    tokens.append("!")
                if "?" in word:
                    word = word[:word.find("?")]
                    tokens.append(word)
                    tokens.append("?")
                if "," in word:
                    word = word[:word.find(",")]
                    tokens.append(word)
                    tokens.append(",")
                if ";" in word:
                    word = word[:word.find(",")]
                    tokens.append(word)
                    tokens.append(",")
                if ":" in word:
                    word = word[:word.find(",")]
                    tokens.append(word)
                    tokens.append(",")
                #else:
                    #tokens.append(word)
    return tokens

text = tokenize("text.txt")
#----------------------------------end of altered code
#print(text)
text_nums = []
wordlist = [".","!",":",";","?","a","the","that","he","she","you","there","though","why","who","what","when","I","me"]#common words are preset
for i in text:
    i = str(i)
    if i in wordlist:
        text_nums.append((wordlist.index(i)))
    else:
        wordlist.append(i)
        text_nums.append((wordlist.index(i)))

#print(text_nums)

def text_to_num(wordlist: List[str],input : List[str]):
    output = []
    for i in input:
        i = str(i)
        if i in wordlist:
            output.append((wordlist.index(i)))
        else:
            wordlist.append(i)
            output.append((wordlist.index(i)))
        return output
    



def num_to_text(text_nums: List[int],wordlist: List[str],input: List[str]):
    output = []
    for i in input:
        if i in text_nums:#if the numerical ID of an input is in the list of all numcerical IDs
            for a in wordlist:
                if wordlist.index(a) == i:#if the index (ID) of a word in the full wordlist is the same as the input
                    output.append(wordlist[i])#add the word that correspondes to the ID to the final output
        else:#if the ID of the input isn't in all of the IDs 
            pass
        return output















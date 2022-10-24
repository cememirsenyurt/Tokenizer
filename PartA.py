from ast import arg
import re
import sys
from nltk.tokenize import word_tokenize
import sys

class WordFrequency():

    #For the tokenize function what we do is going through the text
    # by getting the lines first (let's say the number of lines are n),
    #  and then getting the alphanumeric words from that lines (let's say
    #   the number of alphanumeric characters are m) then going thorugh all these 
    #    with 2 for loops will take O(n.m) time.
    def tokenize(self, file):
        tokens = []
        for line in file:
            for word in re.split(r'(\W+)', line):
                if word.isalnum():
                    word = word.lower()
                    tokens += word_tokenize(word)
        return tokens

    # To compute the word frequency we have to go through every element that
    #  the token list (in our case is list) has. Let's call it n. So, going 
    #   over this list will take O(n) time with 1 for loop.
    def computeWordFrequencies(self,list):
        word_count = {}
        for word in list:
            if word_count.__contains__(word):
                word_count[word] = word_count.get(word) + 1
            else:
                word_count[word] = 1
        return word_count

    # We know that sorted() function in python has O(n.logn) time complexity.
    #  Then, going through the dictionary (that has size n let's say) with 
    #   a for loop is O(n). We'll take the maximum time allocation (worst case scenario)
    #    So, this function runs in O(n. logn) time.
    def print_sorted(self, frequency):
        for word in sorted(frequency, key = lambda k: frequency[k], reverse = True):
            print(word, '-', frequency[word])

if __name__ == '__main__':
    #file = open("a1.txt", "r")
    file = open(sys.argv[1], "r")
    token_object = WordFrequency()
    token_list = token_object.tokenize(file)
    word_freq = token_object.computeWordFrequencies(token_list)
    token_object.print_sorted(word_freq)


    #sort the order in descending order
    #complexity write down comment
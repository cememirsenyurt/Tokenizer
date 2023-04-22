# Tokenizer
Text tokenizer.

Word Frequencies

Method/Function: List<Token> tokenize(TextFilePath)
method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple, aPpLe are the same token). You are allowed to use regular expressions if you wish to (and you can use some regexp engine, no need to write it from scratch), but you are not allowed to import a tokenizer (e.g. from NLTK), since you are being asked to write a tokenizer.

Method:        Map<Token,Count> computeWordFrequencies(List<Token>)
Another method/function that counts the number of occurrences of each token in the token list. Remember that you should write this assignment yourself from scratch so you are not allowed to import a counter when the assignment asks you to write that method.

Method:         void print(Frequencies<Token, Count>)
Finally, a method that prints out the word frequency count onto the screen. The print out should be ordered by decreasing frequency (so, the highest frequency words first). 


Reasonable outputs:
<token>\t<freq>
<token> <freq>
<token> - <freq>
<token> = <freq>
<token> > <freq>
<token> -> <freq>
<token> => <freq>

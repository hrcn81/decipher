from nltk.tokenize import word_tokenize, sent_tokenize

# Text to be tokenized
txt = "Hello Geeks. We're hoping you guys are doing great."

# Tokenize the text into sentences
sentences = sent_tokenize(txt)
print(len(sentences))  # Output: Number of sentences

# Tokenize the text into words
words = word_tokenize(txt)
print(len(words))  # Output: Number of words

# Display all the words
for word in words:
    print(word)  # Output: Each word on a separate line

# Display all the words without punctuation
for word in words:
    if word != '.':
        print(word)  # Output: Each word without punctuation on a separate line

'''
2          # Number of sentences
10         # Number of words
Hello      # Each word on a separate line
Geeks      # Each word on a separate line
.          # Each word on a separate line
We         # Each word on a separate line
're        # Each word on a separate line
hoping     # Each word on a separate line
you        # Each word on a separate line
guys       # Each word on a separate line
are        # Each word on a separate line
doing      # Each word on a separate line
great      # Each word on a separate line
.          # Each word on a separate line
Hello      # Each word without punctuation on a separate line
Geeks      # Each word without punctuation on a separate line
We         # Each word without punctuation on a separate line
're        # Each word without punctuation on a separate line
hoping     # Each word without punctuation on a separate line
you        # Each word without punctuation on a separate line
guys       # Each word without punctuation on a separate line
are        # Each word without punctuation on a separate line
doing      # Each word without punctuation on a separate line
great      # Each word without punctuation on a separate line
'''

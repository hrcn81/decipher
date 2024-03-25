from nltk.tokenize import word_tokenize, sent_tokenize

# Text to be tokenized
txt = "Hello Geeks. We're hoping you guys are doing great."

# Tokenize the text into sentences
sentences = sent_tokenize(txt)
print(len(sentences))  # Output: 2, as there are 2 sentences

# Tokenize the text into words
words = word_tokenize(txt)
print(len(words))  # Output: 10, as there are 10 words

# Display all the words
for word in words:
    print(word)

# Display all the words without punctuation
for word in words:
    if word != '.':
        print(word)

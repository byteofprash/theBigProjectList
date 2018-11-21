
# **Count Words in a String** - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

def count_words(string):
    print(string.split())
    return len(string.split())

print(count_words("What is the meaning of life?           I wish I knew it."))

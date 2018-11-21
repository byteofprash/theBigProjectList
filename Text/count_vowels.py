
# **Count Vowels** - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

string = "What is the meaning of life"
worddict = {'a':0,'e':0,'i':0,'o':0,'u':0}
for x in string:
    if x in ['a','e','i','o','u']:
        worddict[x] +=1

print(worddict)



class PigLatin:
    def getPigLatin(self,string):
        return string[1:]+string[0]+"ay"


pl = PigLatin()
test_words = ["pig","latin","banana","happy" , "duck","me","too","will","real","simple","say","bagel","fail","poo","party","lonely","friends","Lauren"]
for word in test_words:
    print(word+" : ",pl.getPigLatin(word))

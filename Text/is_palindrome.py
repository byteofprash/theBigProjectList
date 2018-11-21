
# **Check if Palindrome** - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

def is_palindrome(string):
    for i in range(1,int(len(string)/2)):
        if string[i-1] == string[-i]:
            continue
        else:
            print(string,"is not a palindrome")
            return 

    print(string,"is a palindrome")


is_palindrome("malayalam")
is_palindrome("racecar")
is_palindrome("tamil")

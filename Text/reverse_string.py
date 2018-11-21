# **Reverse a String** - Enter a string and the program will reverse it and print it out.
class ReverseString:

    def reverseString(self, string):
            return string[::-1]



rs = ReverseString()
data = "üüääü123"
print(rs.reverseString(data))

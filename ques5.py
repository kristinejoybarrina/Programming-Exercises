# Question 5
# Level 1

# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

class String:
    
    def __init__(self):
        self.__string = ""
        
    def getString(self):
        self.__string = str(input("Enter a string: "))
        return self.__string
    
    def printString(self):
        return print (self.__string)
    
my_string = String()

my_string.getString()
my_string.printString()
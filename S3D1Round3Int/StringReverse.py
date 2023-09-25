
def stringReverse():
    inputStr = input("Enter Any String You want to Reverse!:- ")
    str=inputStr[::-1]
    
    # for char in inputStr:
    #     str+=char
    return str


print(stringReverse())
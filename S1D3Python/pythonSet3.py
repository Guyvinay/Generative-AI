# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.


    # - *Output*: "John is 25 years old. Jane is 30 years old."

input= [("John", 25), ("Jane", 30)]

print(f"{input[0][0]} is {input[0][1]}. {input[1][0]} is {input[1][1]}") 

# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    # - *Input*: Add "John": 25, Update "John": 26, Delete "John"
    # - *Output*: "{}, {'John': 26}, {}"

def addName(dictionary , name , age):
    dictionary[name]:age

def updateAge(dictionary , name , age):
    if name in dictionary:
        dictionary[name]=age

def deleteName(dictionary , name):
    if name in dictionary:
        del dictionary[name]


dictionary = {}
addName(dictionary,"Vinay",21)
print(dictionary)
updateAge(dictionary,"Vinay",22)
print(dictionary)
deleteName(dictionary,"Vinay")
print(dictionary)


def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Create an empty dictionary
name_age_dict = {}

# Add a new name-age pair
add_name_age(name_age_dict, "John", 25)
print(name_age_dict)  # Output: {'John': 25}

# Update the age of a name
update_age(name_age_dict, "John", 26)
print(name_age_dict)  # Output: {'John': 26}

# Delete a name from the dictionary
delete_name(name_age_dict, "John")
print(name_age_dict)  # Output: {}

# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
Input= [2, 7, 11, 15]
target = 26
#     - *Output*: "[0, 1]"
Input.sort()
i=0 
j=len(Input)-1
ans=[]
while i<j :
    sumE = Input[i]+Input[j]
    if sumE==target:
        ans.append(i)
        ans.append(j)
        i=i+1
        j=j-1
    elif sumE>target:j=j-1
    else: i=i+1    
print(ans)

# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."
def isPalindrom(str):
    str = ''.join(str.split()).lower()
    return str==str[::-1]
ans=isPalindrom("Madam")
if ans : print("palindrome")
else : print("not a palindrom")

# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
input= [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1 , len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min] = arr[min] ,arr[i] 
    return arr        
ans = selectionSort(input)               
print(ans)

# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
    # Input = push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"
from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, item):
        # Add the item to q1
        self.q1.put(item)

    def pop(self):
        if self.q1.empty():
            return None

        # Move all items from q1 to q2, except the last one
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Get and return the last item from q1 (which is the top of the stack)
        top_item = self.q1.get()

        # Swap q1 and q2 to maintain the stack order
        self.q1, self.q2 = self.q2, self.q1

        return top_item

# Example usage:
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1


# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."
list=[]
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list.append("FizzBuzz")
    elif i % 3 == 0:
        list.append("Fizz")
    elif i % 5 == 0:
        list.append("Buzz")
    else:
        list.append(str(i))
print(" ".join(list))


# Read the input file
with open("E:\VINAY\WEB-DVP\GITHUB-REPO\Generative-AI\S1D3Python\input.txt", "r") as file:
    content = file.read()

# Split the content into words using whitespace as the delimiter and count the words
word_count = len(content.split())

# Write the word count to the output file
with open("E:\VINAY\WEB-DVP\GITHUB-REPO\Generative-AI\S1D3Python\output.txt", "w") as output_file:
    output_file.write(f"Number of words: {word_count}")
    output_file.write("\n")
    output_file.write("Enjoying really")

# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."
def divideNum(a,  b):
    try:
        res = a/b
        return res
    except ZeroDivisionError :
        return "You're Going Beyond your limit, Stay in your limit, do not divide by Zero"
print()
print(divideNum(21 , 0))    
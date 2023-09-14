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

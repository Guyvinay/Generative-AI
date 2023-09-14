#1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
    # - *Input*: "cinema", "iceman"
    # - *Output*: "True"


def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word1 = ''.join(word1.split()).lower()
    word2 = ''.join(word2.split()).lower()
    
    # Check if the sorted characters of both words are equal
    return sorted(word1) == sorted(word2)

# Example usage:
word1 = "cinema"
word2 = "iceman"

result = are_anagrams(word1, word2)
print(result)  # Output: True



# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swap=False
        for j in range(0 , n-i-1):
            if arr[j]>arr[j+1]:
               arr[j], arr[j+1]=arr[j+1],arr[j]
               swap=True
        if not swap:
            break    

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the loop (no swaps in this pass)
        swapped = False

        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in this pass, the list is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]


# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
    # - *Input*: ["flower","flow","flight"]
    # - *Output*: "fl"

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the list
    min_str = min(strs, key=len)

    for i, char in enumerate(min_str):
        for string in strs:
            if string[i] != char:
                return min_str[:i]

    return min_str

# Example usage:
input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)  # Output: "fl"



# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
    # - *Input*: "abc"
    # - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

# def permutation(s):
#     if len(s)<=1:
#         return [s]
#     permut = []
#     for i , char in enumerate(s):
#         remChars = s[:i]+s[i+1:]
#     for perm in permutation(remChars):
#         permut.append(char+perm)    

#     return permut;          

def string_permutations(s):
    if len(s) <= 1:
        return [s]
    
    permutations = []
    for i, char in enumerate(s):
        # Create a substring without the current character
        remaining_chars = s[:i] + s[i+1:]
        
        # Recursively calculate permutations of the remaining substring
        for perm in string_permutations(remaining_chars):
            permutations.append(char + perm)

    return permutations

# Example usage:
input_string = "abc"
permutations = string_permutations(input_string)
print(permutations)


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operation
        self.stack2 = []  # Stack for dequeue operation
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop from stack2 (front of the queue)
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty
    
    def is_empty(self):
        return not (self.stack1 or self.stack2)

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1 (FIFO order)
print(queue.dequeue())  # Output: 2 (FIFO order)

queue.enqueue(4)
print(queue.dequeue())  # Output: 3 (FIFO order)
print(queue.dequeue())  # Output: 4 (FIFO order)
print(queue.dequeue())  # Output: None (Queue is empty)



# ### Problem **1: Print the following pattern**
# Write a program to print the following number pattern using a loop.

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
print()
#2
numsList = [12, 75, 150, 180, 145, 525, 50]
for i in numsList:
    if i>500:
        break
    if i>150:
        continue
    if i%5==0:
        print(i)


# 3. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

def appendString(str1,str2):
    mid=len(str1)//2
    return str1[:mid]+str2+str1[mid:]
print(appendString(str1="vinay",str2="Kumar"))



# 4.Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.


def arrangeletters(str):
    lower = [ch for ch in str if ch.islower() ]
    upper = [ch for ch in str if ch.isupper() ]
    ans=''.join(lower+upper)
    return ans

print(arrangeletters(str="Vinay"))


# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

def addlists(l1 , l2):
    minl=min(len(l1) , len(l2))
    nlist=[]
    for i in range(minl):
        nlist.append(l1[i]+l2[i])

    if len(l1) > minl:
        nlist.extend(l1[minl:])    
    elif len(l2)>minl:
        nlist.extend(l2[minl:])    
    return nlist    

list1 = ["h", "m", "na", "i", "Vinay"]
list2 = ["i", "y", "me", "s"]
print(addlists(list1 , list2))


# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

ansList = [x+y for x in list1 for y in list2]
print(ansList)


# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# 10 400
# 20 300
# 30 200
# 40 100
list2.reverse()
for i , j in zip(list1,list2):
    print(i , j)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {i:defaults.copy()for i in employees}
print(result)


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
keys = ["name", "salary"]
# //expected output

# {'name': 'Kelly', 'salary': 8000}

ans = {key : sample_dict[key] for key in keys }
print(ans)

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
nested_tuple = ((11, [22, 33]), (44, 55))
modified_tuple = (
    (nested_tuple[0][0], [222] + nested_tuple[0][1]),
    nested_tuple[1]
)
print(modified_tuple)
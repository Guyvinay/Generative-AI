print("Hello World")
# 1.Variables of different data types

integer_var = 10
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dictionary_var = {"key": "value"}
set_var = {7, 8, 9}

#2. Printing the types and values of variables
print(f"Type of integer_var: {type(integer_var)}, value: {integer_var}")
print(f"Type of float_var: {type(float_var)}, value: {float_var}")
print(f"Type of string_var: {type(string_var)}, value: {string_var}")
print(f"Type of boolean_var: {type(boolean_var)}, value: {boolean_var}")
print(f"Type of list_var: {type(list_var)}, value: {list_var}")
print(f"Type of tuple_var: {type(tuple_var)}, value: {tuple_var}")
print(f"Type of dictionary_var: {type(dictionary_var)}, value: {dictionary_var}")
print(f"Type of set_var: {type(set_var)}, value: {set_var}")


nList = list(range(1,11))
nList.append(20)
nList.remove(5)
nList.sort()
print(nList)


totalSum = sum(nList)
average = totalSum / len(nList)
print(f"Sum: {totalSum}, Average:{average}")

# String Reversal: Write a Python function that takes a string and returns the string in reverse order.

def stringReverse(string):
 return string[::-1]

ogString = "Python"
revString = stringReverse(ogString)
print(revString)


# 6 Count Vowels: Write a Python program that counts the number of vowels in a given string.


def countVowel(string):
 vowels = "AEIOUaieou"
 cnt = 0
 for c in string :
  if c in vowels:
   cnt+=1
 return cnt

inpString = "hello"
print(f"Number of vowels:-{countVowel(inpString)}")
  
#   7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.

def isPrime(num):
 if num<2:return False
 for i in range(2,int(num*0.5)+1):
  if num%i==0:
   return False
 return True

isPrimeNum = 101
if isPrime(isPrimeNum):
 print(f"{isPrimeNum} is prime number")
else:
 print(f"{isPrimeNum}:- is not prime")


# Factorial Calculation: Write a Python function that calculates the factorial of a number.

def factorial(num):
 if num<0:
  return "factorial is not defined for -ve numbers"
 elif num==0 or num==1:
  return 1
 else:
  result=1
  for i in range(2,num+1):
   result *=i
  return result

factNum = 6
print(f"{factorial(factNum)}")


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibbonaci_num(n):
 fibbSum = 0
 if n<= 0:
  return []
 elif n==1:
  return [0]
 elif n==2:
  return [0,1]
 else:
  seq = [0,1]
  while len(seq) < n :
   nextNum = seq[-1]+seq[-2]
   seq.append(nextNum)
   fibbSum+=nextNum
  return seq

fibbNum = 5
print(f"{fibbonaci_num(fibbNum)}")


# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
   
listCompSquare = [x**2 for x in range(1,11)]
print(listCompSquare)


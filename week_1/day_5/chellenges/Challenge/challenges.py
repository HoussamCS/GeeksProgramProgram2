# Exercice 1
# Insert an item at a defined index in a list
my_list = [1, 2, 3, 4]
index = 2
item = 99
my_list.insert(index, item)
print(my_list)





# Exercice 2:
# Count the number of spaces in a string
text = "Hello world from Python"
count = text.count(' ')
print(count)




# Exercice 3:
# Count uppercase and lowercase letters in a string
text = "HeLLo WorLD"
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)


# Exercice 4:
# Sum of an array without using sum()
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(my_sum([1, 5, 4, 2]))


# Exercice 5:
# Find max number in a list
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([0, 1, 3, 50]))


# Exercice 6:
# Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(4))


# Exercice 7:
# Count an element in a list (without count method)
def list_count(lst, element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count

print(list_count(['a', 'a', 't', 'o'], 'a'))


# Exercice 8:
# L2 norm (square root of sum of squares)
import math

def norm(lst):
    total = 0
    for num in lst:
        total += num ** 2
    return math.sqrt(total)

print(norm([1, 2, 2]))



# Exercice 9:
# Check if array is monotonic
def is_mono(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or \
           all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))


# Exercice 10:
# Print longest word in a list
def longest_word(words):
    return max(words, key=len)

print(longest_word(["apple", "banana", "watermelon"]))


# Exercice 11:
# Separate integers and strings in a list
data = [1, 'hi', 3, 'python', 7, 'world']
ints = [x for x in data if isinstance(x, int)]
strings = [x for x in data if isinstance(x, str)]
print("Integers:", ints)
print("Strings:", strings)


# Exercice 12:
# Check if a string is palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('radar'))
print(is_palindrome('john'))



# Exercice 13:
# Count words with length > k
def sum_over_k(sentence, k):
    words = sentence.split()
    count = 0
    for w in words:
        if len(w) > k:
            count += 1
    return count

sentence = 'Do or do not there is no try'
k = 2
print(sum_over_k(sentence, k))


# Exercice 14:
# Average of dictionary values
def dict_avg(d):
    total = 0
    for v in d.values():
        total += v
    return total / len(d)

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))


# Exercice 15:
# Common divisors of 2 numbers
def common_div(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return divisors

print(common_div(10, 20))


# Exercice 16:
# Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))



# Exercice 17:
# Print elements if index and value are even
def weird_print(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            result.append(lst[i])
    return result

print(weird_print([1, 2, 2, 3, 4, 5]))



# Exercice 18:
# Count types of keyworded arguments
def type_count(**kwargs):
    type_dict = {}
    for value in kwargs.values():
        t = type(value).__name__
        type_dict[t] = type_dict.get(t, 0) + 1
    return type_dict

print(type_count(a=1, b='string', c=1.0, d=True, e=False))




# Exercice 19:
# Mimic split() method
def my_split(s, sep=' '):
    words = []
    current = ''
    for ch in s:
        if ch == sep:
            if current:
                words.append(current)
                current = ''
        else:
            current += ch
    if current:
        words.append(current)
    return words

print(my_split("Hello world from Python"))
print(my_split("apple,banana,grape", ','))



# Exercice 20:
# Convert a string into password format
def hide_password(s):
    return '*' * len(s)

print(hide_password("mypassword"))

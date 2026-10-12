# Exercise 1 : Dictionary Exercises
# (Complete ALL of the following using dictionary comprehension)

# 1. Turn a list of pairs into a dictionary
pairs = [("name", "Elie"), ("job", "Instructor")]
dict1 = {k: v for k, v in pairs}
print(dict1)

# 2. Combine two lists with zip
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dict2 = {k: v for k, v in zip(list1, list2)}
print(dict2)

# 3. Vowels as keys, 0 as values (no fromkeys)
dict3 = {vowel: 0 for vowel in "aeiou"}
print(dict3)

# 4. Letter position as key, letter as value
dict4 = {i: chr(64 + i) for i in range(1, 27)}
print(dict4)

# 5. Super bonus: count the vowels in "awesome sauce"
string = "awesome sauce"
vowels = "aeiou"
dict5 = {vowel: string.count(vowel) for vowel in vowels}
print(dict5)
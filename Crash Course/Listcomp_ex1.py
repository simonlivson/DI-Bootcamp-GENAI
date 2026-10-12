# Exercise: List #1 (list comprehensions)

# 1. Print all values
[print(n) for n in [1, 2, 3, 4]]

# 2. Print values multiplied by 20
[print(n * 20) for n in [1, 2, 3, 4]]

# 3. First letter of each name
print([name[0] for name in ["Elie", "Tim", "Matt"]])
# ['E', 'T', 'M']

# 4. Even values only
print([n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0])
# [2, 4, 6]

# 5. Intersection of two lists
print([n for n in [1, 2, 3, 4] if n in [3, 4, 5, 6]])
# [3, 4]

# 6. Reversed and lowercase
print([word[::-1].lower() for word in ["Elie", "Tim", "Matt"]])
# ['eile', 'mit', 'ttam']

# 7. Letters in both words
print([letter for letter in "first" if letter in "third"])
# ['i', 'r', 't']

# 8. Divisible by 12, from 1 to 100
print([n for n in range(1, 101) if n % 12 == 0])
# [12, 24, 36, 48, 60, 72, 84, 96]

# 9. Remove vowels
print([letter for letter in "amazing" if letter not in "aeiou"])
# ['m', 'z', 'n', 'g']

# 10. Three copies of [0, 1, 2]
print([[n for n in range(3)] for _ in range(3)])
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 11. Ten copies of 0 to 9
print([[n for n in range(10)] for _ in range(10)])

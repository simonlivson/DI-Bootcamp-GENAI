# 1. What is a module?
# A module is a Python file (.py) full of ready-made code, like functions and
# variables, that you can use in another file. Python comes with many built in,
# such as random, math and collections, and you can also write your own.

# 2. Three ways to import a module
# import random                      # import the whole module, then use random.randint()
# from random import randint         # import just one function, then use randint() directly
# import random as rnd               # import with a nickname, then use rnd.randint()
# (A fourth way, from random import *, imports everything but isn't recommended.)

# 3. What is the purpose of importing?
# To reuse code that already exists instead of writing it yourself. It keeps your
# files shorter and organized, and lets you use tools other people already tested.

# 4. Three examples of when you'd use the random module
# - Rolling a dice in a game: random.randint(1, 6)
# - Picking a random winner from a list: random.choice(names)
# - Shuffling a deck of cards or a quiz order: random.shuffle(cards)

# 5. What is an ImportError?
# The error Python gives when an import fails: the module isn't installed, the
# name is misspelled, or you tried to import something the module doesn't have.
# Example: from math import banana  ->  ImportError
# (A completely unknown module gives ModuleNotFoundError, a type of ImportError.)

# 6. When would an OrderedDict be useful?
# When the order of the items matters, for example a ranking or a queue of steps.
# Since Python 3.7 normal dicts also keep their order, but OrderedDict adds extra
# tools like move_to_end(), and treats two dicts with different orders as different.

# 7. When would a defaultdict be useful?
# When you're counting or grouping things and don't want a KeyError for keys that
# don't exist yet. Example: counts = defaultdict(int), then counts[letter] += 1

# 8. What is the purpose of: if __name__ == '__main__':
# It runs the code below it only when you run this file directly, not when
# another file imports it. Python sets __name__ to '__main__' for the file you run,
# and to the module's name when it's imported. That way you can keep tests or demo
# code in a module without them running every time someone imports it.
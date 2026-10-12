# Exercise 1 : Functions Exercises #1

def difference(first_number, second_number):
    return first_number - second_number

def print_day(day_number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= day_number <= 7:
        return days[day_number - 1]   # lists start at 0, so day 1 is days[0]
    return None

def last_element(my_list):
    if my_list:                       # an empty list counts as False
        return my_list[-1]            # -1 means the last item
    return None

def number_compare(first_number, second_number):
    if first_number > second_number:
        return "First is greater"
    elif second_number > first_number:
        return "Second is greater"
    return "Numbers are equal"

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

def list_manipulation(my_list, command, location, value=None):
    if command == "remove":
        if location == "end":
            return my_list.pop()
        if location == "beginning":
            return my_list.pop(0)
    if command == "add":
        if location == "beginning":
            my_list.insert(0, value)
            return my_list
        if location == "end":
            my_list.append(value)
            return my_list

def is_palindrome(text):
    cleaned_text = str(text).replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]    # [::-1] reverses it

def frequency(my_list, search_term):
    return my_list.count(search_term)

def flip_case(text, letter):
    new_text = ""
    for character in text:
        if character.lower() == letter.lower():
            new_text += character.swapcase()
        else:
            new_text += character
    return new_text

def multiply_even_numbers(numbers):
    product = 1
    for number in numbers:
        if number % 2 == 0:
            product *= number
    return product

def mode(numbers):
    return max(set(numbers), key=numbers.count)

def capitalize(word):
    return word[:1].upper() + word[1:]

def compact(my_list):
    return [item for item in my_list if item]

def partition(my_list, callback):
    true_list = []
    false_list = []
    for item in my_list:
        if callback(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return [true_list, false_list]

def is_even(number):
    return number % 2 == 0

def intersection(first_list, second_list):
    return [item for item in first_list if item in second_list]

def once(original_function):
    def inner(*arguments):
        if not inner.has_run:
            inner.has_run = True
            return original_function(*arguments)
        return None
    inner.has_run = False
    return inner

def add(first_number, second_number):
    return first_number + second_number

one_addition = once(add)

# Super bonus: decorator
def run_once(original_function):
    def inner(*arguments):
        if not inner.has_run:
            inner.has_run = True
            return original_function(*arguments)
        return None
    inner.has_run = False
    return inner

@run_once
def add_once(first_number, second_number):
    return first_number + second_number


# Tests
print(difference(2, 2), difference(0, 2))
print(print_day(4), print_day(41))
print(last_element([1, 2, 3, 4]), last_element([]))
print(number_compare(1, 1), number_compare(1, 2), number_compare(2, 1))
print(single_letter_count('amazing', 'A'))
print(multiple_letter_count("hello"))
print(list_manipulation([1, 2, 3], "remove", "end"))
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print(list_manipulation([1, 2, 3], "add", "end", 30))
print(is_palindrome('tacocat'), is_palindrome('robert'))
print(is_palindrome('a man a plan a canal Panama'))
print(frequency([1, 2, 3, 4, 4, 4], 4))
print(frequency([True, False, True, True], False))
print(flip_case("Hardy har har", "h"))
print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
print(capitalize("tim"), capitalize("matt"))
print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
print(partition([1, 2, 3, 4], is_even))
print(intersection([1, 2, 3], [2, 3, 4]))
print(one_addition(2, 2), one_addition(2, 2), one_addition(12, 200))
print(add_once(2, 2), add_once(2, 20), add_once(12, 20))
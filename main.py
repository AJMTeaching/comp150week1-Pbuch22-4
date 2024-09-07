# ------------------------------------------------------------------------

# Lab 1
# Problem 1
my_list = [1, 5, 'apple', 20.5]

        # index print apple 
def search_elements(lst: list[int]) -> int:
     """Searching for an element in the list."""
      if 'apple' in lst:
          return lst.index('apple')
      else:
          return -1
print(sreach_elements(['apple']))

        # append 10
def add_elements(lst: list[int]) -> list[int]:
       """Adding elements to the list."""
       lst.append(10)
       return lst
print(add_elements([10]))

       # remove 20.5
def remove_elements(lst: list[int]) -> list[int]:
      """Removing elements from the list."""
       lst.remove(20.5)
      return lst
print(remove_elements([20.5])
      
      # reversing the list
reversed_my_list = list(reversed(my_list))
#printing the list
print(reversed_my_list)
      

# Problem 2
        # create dictionary 
person= dict({'name': 'john', 'age': 30, 'job': 'teacher'})

        #print vlaue for job
for value,key in job.items():
    if key == job :
         print(teacher)

        # added a new key-pair
person= dict({'name': 'john', 'age': 30, 'job': 'teacher'})
print(&quot;Current Dict is: &quot;, person) 

dict['name'] = 'john'
dict['age'] = '30'
dict['job'] = 'teacher'
dict['city'] = 'paris'
print(&quot;Updated Dict is: &quot;, person)

        # removed key-pair
 del me['age']
print("The dictionary after remove is : ", person)

        # itirate on sperate lines 
person= dict({'name': 'john', 'age': 30, 'job': 'teacher'})
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
// program to count the number of vowels in a string

// defining vowels
const vowels = ["a", "e", "i", "o", "u"]

function countVowel(str) {
    // initialize count
    let count = 0;

    // loop through string to test if each character is a vowel
    for (let letter of str.toLowerCase()) {
        if (vowels.includes(letter)) {
            count++;
        }
    }

    // return number of vowels
    return count
}

// take input
const string = "lets try this" ;

const result = countVowel(string);

console.log(result);

    Returns:
    - int: The number of vowels in the string
    """

    # TODO: Implement this function
    pass

# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.
# using heapq.merge()
 
# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
 
    Parameters:
test_list1 = [8, 7, 6, 10, 5]
test_list2 = [1, 6, 9, 3, 11]

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
res = list(merge(test_list1, test_list2))

# printing result
print("The combined sorted list is : " + str(res))

    """
    # TODO: Implement this function
    pass

# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    string_list= [ "hello", "world", "this", "is", "python"]
    print(len(string_list))

    Returns:
    - list: A list containing the lengths of the words
    """
    # TODO: Implement this function
    pass


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
       Parameters:
    - s (str): The input string
    Reverse a string.
original_string = "I, hate, pineapple"
reversed_string = ''
index = len(original_string) - 1

while index >= 0:
  reversed_string += original_string[index]
  index -= 1

    Returns:
    - str: The reversed string
print("Original String:", original_string)
print("Reversed String:", reversed_string)
    """
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.
    
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# Driver Code
lst1 = [10, 11, 12, 13, 14, 15, 16, 17, 18]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Returns:
    - list: The intersection of the two lists
    print(intersection(lst1, lst2))
    """
    # TODO: Implement this function
    pass


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()

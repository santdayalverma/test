"""Problem 1: Counting the Frequency of Elements in a List"""

# Solution
def count_elements(lst):
    frequency = {}
    for element in lst:
        frequency[element] = frequency.get(element, 0) + 1
    return frequency

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2, 4]
frequency = count_elements(numbers)
print(frequency)  # Output: {1: 3, 2: 3, 3: 2, 4: 2} 
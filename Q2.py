# Min-Max Normalization
#  Write a Python function that takes a list of numbers and returns a normalized version using min-max scaling.
def min_max_normalize(numbers):
    if not numbers:
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    # Handle the case where all values are the same
    if min_val == max_val:
        return [0.0 for _ in numbers]

    normalized = [(x - min_val) / (max_val - min_val) for x in numbers]
    return normalized
data=[10,20,30,40,50]
print(min_max_normalize(data))
from collections import Counter

def count_characters_pythonic(text: str) -> Counter:
    # Counter handles everything: iterating, initializing, and counting.
    return Counter(text)

# --- Example Usage ---
input_string = "kushal sharma"
char_counts = count_characters_pythonic(input_string)

print(char_counts)

# You can access counts like a dictionary
#print(f"The count of 'l' is: {char_counts['l']}") # Output: 3
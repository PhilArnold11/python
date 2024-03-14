def main():
# Example string
    # TODO: Iterate through the string and print each character
    example_string = "Hello, Python programmers!"
    for character in example_string:
        print("Iterating through the string:", character)
    # TODO: Find and print the character with the minimum ASCII value in the string
    min_char = min(example_string)
    print("\nCharacter with the minimum ASCII value:", min_char)
# TODO: Find and print the character with the maximum ASCII value in the string
    max_char = max(example_string)
    print("\nCharacter with the maximum ASCII value:", max_char)
# TODO: Find and print the index of the first occurrence of 'o' in the string
    first_o = example_string.index('o')
    print("\nIndex of 'o':", first_o)
# TODO: Convert the string into a list of characters and print the list
    stoc = list(example_string)
    print("\nConverting string to a list of characters:", stoc)
# TODO: Count and print the number of occurrences of 'o' in the string
    occo = example_string.count('o')
    print("\nCount of 'o' in the string:", occo)
main()

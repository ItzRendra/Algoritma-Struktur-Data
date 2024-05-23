def find_longest_word(string):
    # Split the string into a list of words
    words = string.split()
    
    # Initialize the longest word variable
    longest_word = ""
    
    # Loop through the list of words
    for word in words:
        # If the length of the current word is greater than the longest word
        if len(word) > len(longest_word):
            # Update the longest word
            longest_word = word
    
    # Return the longest word
    return longest_word

# Get the string input from the user
input_string = input("Enter a string: ")

# Call the find_longest_word function with the input string
result = find_longest_word(input_string)

# Print the result
print(f"The longest word in the string '{input_string}' is '{result}'.")
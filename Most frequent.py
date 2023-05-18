# Python code to create a function called most_frequent that takes a string
# and prints the letters in decreasing order of frequency using dictionaries.

def most_frequent(string):
    # Create an empty dictionary to store the frequency of each letter
    letter_freq = {}
    
    # Count the frequency of each letter in the string
    for letter in string:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    
    # Sort the dictionary by values (frequency) in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Print the letters in decreasing order of frequency
    for letter, freq in sorted_freq:
        print(letter, "-", freq)

most_frequent("My name is Akash Pradeep Kumar Pasi.")


    

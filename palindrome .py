# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read the strings from the input file
    strings = [string.strip() for string in infile.readlines()]

    for string in strings:
        # Check if the string is a palindrome
        if string == string[::-1]:   
            outfile.write(string + ' is a palindrome\n')   
        else:   
            outfile.write(string + ' is not a palindrome\n') 

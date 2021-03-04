# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

if __name__ == '__main__':
    fhand = open('romeo.txt')
    new_list = []
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in new_list:
                new_list.append(word)
    new_list.sort()
    print(new_list)
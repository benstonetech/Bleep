from cs50 import get_string
from sys import argv


def main():
    # Initialise a variable
    filtered_string = " "

    # If the command line has the correct amount of arguements
    if len(argv) == 2:

        # Prompt the user to enter a string to test
        my_string = get_string("Enter phrase: ")

        # Split the string into a list at each space
        split_string = my_string.split(" ")

        # Strip words from the file written in argv[1] and put them in a list
        banned_words = [word.rstrip('\n') for word in open(argv[1])]

        # Loop through the list to make them all lower case for easier comparison
        for x in banned_words:
            x = x.lower()

        # Loop throught the list, check wether the lower case version of the element is
        # in the list of banned words. If it is replace the word with the right amount
        # of stars if not add a space
        for y in range(len(split_string)):
            if split_string[y].lower() in banned_words:
                split_string[y] = ("*" * len(split_string[y])) + " "
            else:
                split_string[y] = split_string[y] + " "

        # Concatenate the string back together
        for y in split_string:
            filtered_string = filtered_string + y

        # Print the new concatenated string
        print(filtered_string)
    else:

        # Prompt user usage was incorrect and exit with code 1
        print("Usage: bleep.py list.txt")
        exit(1)


if __name__ == "__main__":
    main()


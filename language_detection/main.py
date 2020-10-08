from textblob import TextBlob
from textblob.exceptions import TranslatorError

import pycountry
import sys

my_dictionary = {}


def import_from_database(file, language):
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        my_dictionary[line] = language

    return my_dictionary


def main():
    print("Welcome to language detection! I will detect your language.")

    while True:
        user_input = input("\nPlease write something in sentence or type >>#exit<< to leave\n")
        if user_input == "#exit": sys.exit("Goodbye!")

        if detect_language(user_input):  # If detect_language is false, skip
            print("The detected language is: " + detect_language(user_input))


def detect_language(user_input):
    # accuracy is guaranteed
    if user_input in my_dictionary.keys():
        return my_dictionary[user_input]
    else:
        # accuracy is not guaranteed, but this library has a good accuracy for longer sentences
        # print("I am sorry, your sentence is not in our database. We will continue with TextBlob-Library")
        b = TextBlob(user_input)
        try:
            iso_code = b.detect_language()
        except TranslatorError:
            sys.stderr.write("Oops! Please provide a string with at least 3 characters.\n")
            return False
    language = pycountry.languages.get(alpha_2=iso_code)
    return language.name


if __name__ == '__main__':
    import_from_database("databases/deu.txt", "German")
    import_from_database("databases/eng.txt", "English")
    import_from_database("databases/por.txt", "Portuguese")
    main()
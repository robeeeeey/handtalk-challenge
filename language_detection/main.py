from textblob import TextBlob
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
    print("Welcome to language detection! I will detect your language.\n")

    while True:
        user_input = input("Please write a sentence or type >#exit< to leave\n")

        if user_input == "#exit": sys.exit("Goodbye!")
        if len(user_input) < 3:
            sys.stderr.write("Oops! Please provide a string with at least 3 characters.\n")
            continue

        print("The detected language is: " + detect_language(user_input))


def detect_language(user_input):
    # accuracy is guaranteed
    if user_input in my_dictionary.keys():
        return my_dictionary[user_input]
    else:
        # accuracy is not guaranteed, but this library has a good accuracy for longer sentences
        b = TextBlob(user_input)
        iso_code = b.detect_language()
    language = pycountry.languages.get(alpha_2=iso_code)
    return language.name


if __name__ == '__main__':
    import_from_database("databases/deu.txt", "German")
    import_from_database("databases/eng.txt", "English")
    import_from_database("databases/por.txt", "Portuguese")
    main()
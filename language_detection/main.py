from textblob import TextBlob
import pycountry
import sys

dictionary = {}


def import_from_database(file, language):
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        dictionary[line] = language

    # print(dictionary)
    return dictionary


def main():
    print("Welcome to language detection! I will detect your language.")

    while True:
        user_input = input("\nPlease write something in sentence or type >>#exit<< to leave\n")
        if user_input == "#exit": sys.exit("Goodbye!");
        print("The detected language is: " + detect_language(user_input))


def detect_language(user_input):
    # accuracy is guaranteed
    if user_input in dictionary.keys():
        return dictionary[user_input]
    else:
        # accuracy is not guaranteed, but this library has a good accuracy for longer sentences
        # print("I am sorry, your sentence is not in our database. We will continue with TextBlob-Library")
        b = TextBlob(user_input)
        iso_code = b.detect_language()
        language = pycountry.languages.get(alpha_2=iso_code)
        return language.name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import_from_database("databases/deu.txt", "German")
    import_from_database("databases/eng.txt", "English")
    import_from_database("databases/por.txt", "Portuguese")
    main()

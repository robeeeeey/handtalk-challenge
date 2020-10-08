# Handtalk Challenge - Strategy



## Analysis & Research

- Understanding the problem
- Research on how to solve the problem



Ideas:

- Looking for a library that can detect language.
- Using the given database for pre-import.
- Create a small CLI with user's input.



## User Flow Diagram
![User Task Diagram](https://github.com/robeeeeey/handtalk-challenge/blob/main/docs/diagram.svg)

The idea of the system is that it will detect the language of the user's input. To leave the interaction you can type #exit.  

## The Code

`main.py` is the main file of the script. 



The method `main()` initializes the script with a while loop for CLI. You can write any sentences you want and the method `detect language(user_input)` is called to determine the language of your input. If you want to exit the script, type "#exit". The given databases provide the following languages: Portuguese, English and German.



The method ```import_from_database(file, language)``` imports the given database from a textfile into a dictonary. It is a collection, that has keys and values which enables you to access the items. `Key` is the lexical/sentence and `Value` is the corresponding language.  



The method `detect_language(user_input)` detects the language of the user's input. It is evaluated, if the input exists in the dictonary,which was imported and saved from the given databases before. If true, it returns the corresponding language. Otherwise the system will detect the the input's corresponding language with a library, called Textblob. Although the accuracy cannot be promised, especially in single words, and at least 3 characters are required. The result is returned in ISO Code (2-letter codes), and the aim is to make it readable. So that is why `pycountry` is used to translate into the language's full name.



IDE: PyCharm (IntelliJ)



## Python Unit Tests

### Testcases:

- Test if, the import works properly.
- Test if, the items are accessible from the list.
- Test if, the returned value is correct.
- Test whether, a Portuguese sentence is detected correctly.
- Test whether, an English sentence is detected correctly.
- Test whether, a German sentence is detected correctly.
- Test whether, a Japanese sentence is detected correctly.
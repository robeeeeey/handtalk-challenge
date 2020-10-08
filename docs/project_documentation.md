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



The method `main()` initializes the script with a while loop for CLI. You can enter anything you want in sentence and the method `detect language(user_input)` is called to determine the language of your input. If you want to exit the script, type "#exit". The given databases provide the following languages: Portuguese, English and German.



The method `import_from_database(file, language)` imports the given database from a textfile into a dictonary. It is a collection and it has keys and values which you can access the items. `Key` is the lexical and `Value` is the language.  



The method `detect_language(user_input)` detects the language of the user's input. First it checks from the dictionary, which was imported and saved from the given databases. If there is no key in the list, the system will detect the language with a library called Textblob.  But the accuracy cannot be promised, especially in shorter sentences or single words, and at least 3 characters are needed. The result is returned in ISO Code, and we want to make it readable. So that is why `pycountry` is needed to translate in the full name of the language.



## Testing 


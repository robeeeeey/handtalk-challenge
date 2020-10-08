import unittest
from main import import_from_database, detect_language


class MyTestCase(unittest.TestCase):
    def test_import(self):
        pt_dictionary = import_from_database("databases/por.txt", "Portuguese")
        en_dictionary = import_from_database("databases/eng.txt", "English")
        ger_dictionary = import_from_database("databases/deu.txt", "German")

        self.assertTrue(len(pt_dictionary) > 0)
        self.assertEqual(pt_dictionary.get("Oi."), "Portuguese")

        self.assertTrue(len(en_dictionary) > 0)
        self.assertEqual(en_dictionary.get("Hi."), "English")

        self.assertTrue(len(ger_dictionary) > 0)
        self.assertEqual(ger_dictionary.get("Hallo!"), "German")

    def test_portuguese(self):
        language = "Portuguese"
        import_from_database("databases/por.txt", language)
        self.assertEqual(detect_language("Vai."), language)
        self.assertEqual(detect_language("Eu gosto de café."), language)
        self.assertEqual(detect_language("Além do horizonte."), language)

    def test_english(self):
        language = "English"
        import_from_database("databases/eng.txt", language)
        self.assertEqual(detect_language("Hi."), language)
        self.assertEqual(detect_language("I like coffee."), language)

    def test_german(self):
        language = "German"
        import_from_database("databases/deu.txt", language)
        self.assertEqual(detect_language("Hallo!"), language)
        self.assertEqual(detect_language("Ich mag Kaffee."), language)
        self.assertEqual(detect_language("Deutsche Sprache, schwere Sprache."), language)

    def test_japanese(self):
        language = "Japanese"
        self.assertEqual(detect_language("こんにちは"), language)
        self.assertEqual(detect_language("コーヒーが好き."), language)


if __name__ == '__main__':
    unittest.main()

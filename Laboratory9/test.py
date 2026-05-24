import unittest
from lab9level3variant3 import Trie, build_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.patterns = ["apple", "app", "apricot", "banana"]
        self.trie = build_trie(self.patterns)

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("orange"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))

    def test_starts_with_non_existing_prefix(self):
        self.assertFalse(self.trie.starts_with("bat"))

    def test_insert_new_word(self):
        self.trie.insert("batman")
        self.assertTrue(self.trie.search("batman"))
        self.assertTrue(self.trie.starts_with("bat"))


if __name__ == "__main__":
    unittest.main()
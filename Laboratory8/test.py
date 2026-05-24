import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab8level2variant3 import solve_wchain, main

class TestWChain(unittest.TestCase):
    
    def _run_full_cycle(self, words: list[str], expected_result: int):
        """Функція створює файл wchain.in і вписує туди слова з тестів."""
        file_content = f"{len(words)}\n" + "\n".join(words) + "\n"
        
        with open("wchain.in", "w") as f:
            f.write(file_content)
            
        main()
        
        with open("wchain.out", "r") as f:
            result = f.read().strip()
            
        self.assertEqual(int(result), expected_result)

    def test_example_1(self):
        words = ["word", "anotherword", "yetanotherword"]
        self._run_full_cycle(words, 1)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self._run_full_cycle(words, 4)

    def test_example_3(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self._run_full_cycle(words, 6)

    # def tearDown(self):
    #     if os.path.exists("wchain.in"):
    #         os.remove("wchain.in")
    #     if os.path.exists("wchain.out"):
    #         os.remove("wchain.out")

if __name__ == '__main__':
    unittest.main()
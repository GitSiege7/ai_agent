import unittest
from functions.get_file_content import get_file_content

class TestGetContent(unittest.TestCase):
    def test(self):
        print("Test 1:")
        print(get_file_content("calculator", "main.py"))
        print()

    def test2(self):
        print("Test 2:")
        print(get_file_content("calculator", "pkg/calculator.py"))
        print()

    def test3(self):
        print("Test 3:")
        print(get_file_content("calculator", "/bin/cat"))
        print()

    def test4(self):
        print("Test 4:")
        print(get_file_content("calculator", "lorem.txt"))
        

if __name__ == "__main__":
    unittest.main()
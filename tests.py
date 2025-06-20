import unittest
from functions.run_python import run_python_file

class TestGetContent(unittest.TestCase):
    def test(self):
        print("Test 1:")
        print(run_python_file("calculator", "main.py"))
        print()

    def test2(self):
        print("Test 2:")
        print(run_python_file("calculator", "tests.py"))
        print()

    def test3(self):
        print("Test 3:")
        print(run_python_file("calculator", "../main.py"))
        print()

    def test4(self):
        print("Test 4:")
        print(run_python_file("calculator", "nonexistent.py"))
        print()


if __name__ == "__main__":
    unittest.main()
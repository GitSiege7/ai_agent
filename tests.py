import unittest
from functions.write_file import write_file

class TestGetContent(unittest.TestCase):
    def test(self):
        print("Test 1:")
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
        print()

    def test2(self):
        print("Test 2:")
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
        print()

    def test3(self):
        print("Test 3:")
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
        print()


if __name__ == "__main__":
    unittest.main()
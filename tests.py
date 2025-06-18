import unittest
from functions.get_files_info import get_files_info

class TestGetFiles(unittest.TestCase):
    def test(self):
        print("Test 1:")
        print(get_files_info("calculator", "."))
        print("\n")

    def test2(self):
        print("Test 2:")
        print(get_files_info("calculator", "pkg"))
        print("\n")

    def test3(self):
        print("Test 3:")
        print(get_files_info("calculator", "/bin"))
        print("\n")

    def test4(self):
        print("Test 4:")
        print(get_files_info("calculator", "../"))
        print("\n")

if __name__ == "__main__":
    unittest.main()
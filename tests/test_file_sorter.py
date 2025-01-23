import os
import shutil
import unittest
from task1_file_sorter.file_sorter import copy_files_by_extension, create_directory

class TestFileSorter(unittest.TestCase):

    def setUp(self):
        # Створення тестової структури директорій
        self.test_source_dir = "test_source"
        self.test_destination_dir = "test_destination"
        create_directory(self.test_source_dir)
        create_directory(self.test_destination_dir)

        # Додавання тестових файлів
        self.test_files = [
            "file1.txt",
            "file2.doc",
            "file3.txt",
            "image1.png",
            "archive1.zip",
        ]

        for file in self.test_files:
            with open(os.path.join(self.test_source_dir, file), "w") as f:
                f.write("Test content")

    def tearDown(self):
        # Видалення директорій після тесту
        shutil.rmtree(self.test_source_dir)
        shutil.rmtree(self.test_destination_dir)

    def test_copy_files_by_extension(self):
        # Виконання функції сортування
        copy_files_by_extension(self.test_source_dir, self.test_destination_dir)

        # Перевірка, що файли сортуються за розширенням
        for file in self.test_files:
            ext = os.path.splitext(file)[1].lstrip(".") or "others"
            expected_dir = os.path.join(self.test_destination_dir, ext)
            self.assertTrue(os.path.exists(expected_dir), f"Directory {expected_dir} does not exist.")

            expected_file = os.path.join(expected_dir, file)
            self.assertTrue(os.path.exists(expected_file), f"File {expected_file} does not exist.")

if __name__ == "__main__":
    unittest.main()
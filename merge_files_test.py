import mail
import unittest

class TestMergingFiles(unittest.TestCase):
    """docstring for TestMergingFiles"""
    def test_merge_files(self):
        file_to_read1 = "FMI.txt"
        file_read1 = open(file_to_read1, "r")
        content1 = file_read1.read()
        file_read1.seek(0)
        file_to_write = "merge"
        file_write = open(file_to_write, "w")
        file_to_read2 = "Hack Bulgaria.txt"
        file_read2 = open(file_to_read2, "r")
        content2 = file_read2.read()
        file_read2.seek(0)
        data = content1 + content2
        file_write.write(data)

        self.assertEqual(file_read1.read() + file_read2.read(), mail.merge_files("FMI.txt", "Hack Bulgaria.txt").show_list_content)
        file_read1.close()
        file_read2.close()
        file_write.close()


if __name__ == '__main__':
    unittest.main()



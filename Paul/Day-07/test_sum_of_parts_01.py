

import unittest
import os

from sum_of_parts_01 import Instruction, get_input, initialize


initialize("ERROR")

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'test.txt')


class ReadFile(unittest.TestCase):

    def test_read_file_and_dependency_list(self):
        dependency_list = get_input(TESTDATA_FILENAME)
        self.assertIn(("C", "A"), dependency_list)   # test first line in file
        self.assertIn(("A", "D"), dependency_list)   # test middle line in file
        self.assertIn(("F", "E"), dependency_list)   # test last line in file


class TestInstruction(unittest.TestCase):

    def setUp(self):
        self.instruction = Instruction("A")

    def test_create_instruction_name(self):
        self.assertEqual("A", self.instruction.name)

    def test_add_dependency(self):
        self.instruction.add_dependency("B")
        self.assertEqual(set("B"), self.instruction.dependencies)

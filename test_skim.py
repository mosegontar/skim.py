import os
import unittest
from skim import skim


TEST_CODE1 = """


class FirstClass(object):

    def __init__(self, arg1):
        self.arg1 = arg1

    def print_arg(self):
        print(self.arg1)
        return True

class SecondClass(FirstClass):

    def printhey(sentence):
        print('Say hey')

def main():

    for i in range(x):
        if i+i=i:
            return done

if __init__=='__main__':
    main()

"""

class TestSkim(unittest.TestCase):

    def setUp(self):
        self.f = open('_temp.py', 'w')
        self.cwd = os.getcwd()

    def tearDown(self):
        os.remove(self.f.name)

    def write_contents(self, content):
        self.f.write(content)
        self.f.close()

    def test_that_skim_returns_list_all_correct_classes_and_defs_with_correct_spacing(self):

        self.write_contents(TEST_CODE1)

        excepted_returned_list = ['class FirstClass(object):', '    def __init__(self, arg1):',
                                   '    def print_arg(self):', 'class SecondClass(FirstClass):',
                                   '    def printhey(sentence):', 'def main():']

        returned_list = skim.process_files('_temp.py')[0]

        self.assertEqual(excepted_returned_list, returned_list)

    def test_that_skim_correctly_identifies_longest_line(self):

        self.write_contents(TEST_CODE1)
        
        matches = skim.process_files('_temp.py')
        results = [matches]

        self.assertEqual(skim.determine_longest_matched_line(results), 30)



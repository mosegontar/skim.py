import os
import sys
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

TEST_CODE2 = """

from foo import bar

def say_hey():
    return 'bar'

def do_stuff(key=value): # this function says bye
    def make_thing(thing)
        print(key, thing)
    return make_thing

print('i woke up early on my born day')

class HumanBody(object):

    class Meta:
        some_random_meta_data = data

    def a(b, c, d, e):
        return b + c + d +e

"""

TEST_CODE3 = """

def hello(operator):
    print('hi operator')

"""

TEST_CODE4 = """

# Something something something

## yada yada yada

### blah blah blah

"""


class TestSkim(unittest.TestCase):

    def setUp(self):
        self.open_files = []
        self.cwd = os.getcwd()

    def tearDown(self):
        for f in self.open_files:
            os.remove(f.name)

    def write_contents(self, *filecontents):
        for index, text in enumerate(filecontents):
            with open(self.cwd+'/_f{}.py'.format(index), 'w') as f:
                f.write(text)
                f.close()
                self.open_files.append(f)


    def test_returns_nothing_if_passed_file_with_no_matches(self):
        self.write_contents(TEST_CODE4)
        self.assertFalse(skim.process_files('_f0.py'))

    def test_that_skim_returns_list_all_correct_classes_and_defs_with_correct_spacing(self):
        self.write_contents(TEST_CODE1)

        excepted_returned_list = ['class FirstClass(object):', '    def __init__(self, arg1):',
                                  '    def print_arg(self):', 'class SecondClass(FirstClass):',
                                  '    def printhey(sentence):', 'def main():']



        returned_list = skim.process_files('_f0.py')[0]

        self.assertEqual(excepted_returned_list, returned_list)

    def test_that_skim_correctly_identifies_longest_line(self):
        self.write_contents(TEST_CODE1)
        
        matches = skim.process_files('_f0.py')
        results = [matches]

        self.assertEqual(skim.determine_longest_matched_line(results), 30)



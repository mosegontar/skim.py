#!/usr/bin/python
import sys
import os
import re


def print_matches(matches, filename, length):

    print(filename.center(length, '-'))
    print
    for line in matches:
        print(line)
    print
    print(filename.center(length, '-'))


def check_regex(line):
    match = re.match('^\s*class.*:', line) or re.match('^\s*def.*:', line)
    try:
        return match.group()
    except AttributeError:
        return None

def get_match(contents):
    matches = [check_regex(line) for line in contents if check_regex(line)]
    return matches

def read_file_contents(filename):
    
    try:
        with open(filename, 'r') as f:
            content = f.readlines()
    except EnvironmentError as e:
        raise e
    
    return content

def process_files(filename):
    contents = read_file_contents(filename)
    matches= get_match(contents)    
    return (matches, filename, len(max(matches, key=len)))

def main():
    
    results = []
    for arg in sys.argv[1:]:
        files = process_files(arg)
        results.append(process_files(arg))
    if not results:
        return

    longest = max(results, key=lambda x: x[2])[2]
    for result in results:
        print_matches(result[0], result[1], longest)

if __name__ == '__main__':
    main()


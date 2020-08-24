#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Wesley Salesberry"


import random
import sys


def create_mimic_dict(filename):
    word_list = {}
    with open(filename) as f:
        line = f.read()
        words = line.split()

    words_length = len(words)

    for element in range(words_length - 1):
        if words[element] not in word_list:
            word_list[words[element]] = [words[element + 1]]
        else:
            word_list[words[element]].append(words[element+1])
        continue
    word_list[''] = [words[0]]

    return word_list


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        X Use a start_word of '' (empty string)
        X Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    # +++your code here++
    # random_words = random.sample(list(mimic_dict), num_words)
    # words = " ".join(random_words)

    word = [mimic_dict[''][0]]

    for _ in range(num_words - 1):
        value_word = mimic_dict.get(word[-1], mimic_dict[''][0])
        next_word = random.choice(value_word)
        word.append(next_word)
    print(" ".join(word), end=" ")


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')

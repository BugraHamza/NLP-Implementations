#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Binary Classifier
 is a decider if a sentence ends.
 
 Algorithm:
    1) Set the stop punctuations.
    2) Set the abbreviations.
    3) Check if the punctuation is in the abbreviation list, and
        the word is at the end.
    4) Check the word ends with a period.
    5) Append EOS word into list
    6) Return the list.
'''

def is_EOS(text, abbreviation_list = ['Dr.', 'Inc.', 'e.g.', 'i.e.', 'a.m.', 'p.m.']):
    stops = '.?!'
    text_list = text.split()
    EOS_words = []
    for index, word in enumerate(text_list):
        if word in abbreviation_list:
            if index == len(text_list) - 1:
                EOS_words.append([word, index])
        elif '...' in word:
            if '...' != word and ',' != text_list[index - 1][-1]:
                EOS_words.append([word, index])
        elif word[-1] in stops:
            EOS_words.append([word, index])

    return EOS_words

if __name__ == '__main__':
    sentence = "I like eating apples."
    words = is_EOS(sentence, ['vb.'])
    print(words)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Porter's Algorithm
 is the most common English stemmer

This code is a simple implementaion of the algorithm.

The main idea is to remove the affixes:
    cats -> cat
    walking -> walk
    relational -> relate
    *activate -> activ 

*Some words are stemmed to be similar the original word such as ponies -> poni,
the letter changes are ignored, but the stems are still understandable

3 main steps:
    Step 1a:
        -sses -> -ss
        -ies -> -i
        -ss -> -ss
        -s -> -
        
    Step 1b:
        (*v*)ing -> (*v*)
        (*v*)ed -> (*v*)
    
    Step 2: (for long stems)
        -ational -> -ate
        -izer -> -ize
        -ator -> -ate
        
    Step 3: (for long stems)
        -al -> -
        -able -> -
        -ate -> -

*v* means verb stem and the stem must contain at least one vowel or 'y'

This steps are based on Standford NLP Course:
 https://www.youtube.com/watch?v=oWsMIW-5xUc&list=PLLssT5z_DsK8HbD2sPcUIDfQ7zmBarMYv     
        
'''

def contains_vowel(word):
    vowels='aeiouy'
    for v in vowels:
        if v in word:
            return True
    return False


def porter_stemmer(word, is_verb=False):
    noun_suffixes = [['sses', 'ss'], ['ies', 'i'], ['ss', 'ss'], ['s', ''],     #STEP 1
                     ['ational', 'ate'], ['izer', 'ize'], ['ator', 'ate'],      #STEP 2
                     ['al', ''], ['able', ''], ['ate', '']]                     #STEP 3
    verb_suffixes = [['ing', ''], ['ed', '']]
    
    if is_verb:
        for suffix, transform in verb_suffixes:
            length = len(suffix)
            if word[-length:] == suffix and contains_vowel(word[:-length]):
                return word[:-length] + transform
        return word
    
    for suffix, transform in noun_suffixes:
        length = len(suffix)
        if word[-length:] == suffix and contains_vowel(word[-length:]):
            return word[:-length] + transform
    return word

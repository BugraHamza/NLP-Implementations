#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Maximum Matching Algorithm
    is an algorithm which is used to find the longest possible word in a sentence.
    This algorithm takes a sentence and a dictionary and 
    finds the words based on the dictionary.
    The algorithm is used for languages that have no spaces such as Chinese.
    
    E.g.
    A given sentence without spaces: 
        Themanwalksbytheriver
    and a dictionary which contains ['The', 'man', 'walks', 'by', 'river', ...]
    
    Algorithms finds the first longest possible word : The
    Then : man
    and moves forward.
    
    :param sentence: The sentence without spaces
    :param dictionary: A wordlist of the language
    :return: The words as a list            
'''

def max_match(sentence, dictionary):
    length = len(sentence)
    word_list = []
    i, j = 0, 0
    
    while i < length:
        word = sentence[i:length - j]
        if word.lower() in dictionary:
            word_list.append(word)
            i, j = i + len(word), 0
        else:
            j += 1
    return word_list

if __name__ == '__main__':
    sentence = 'Thetabledownthere'
    dictionary = ['down', 'in', 'table', 'theta', 
                  'what', 'cat', 'a', 'the', 'book', 
                  'hat', 'i', 'there', 'is', 'bled',
                  'bottle', 'have', 'up', 'drink', 
                  'own','dude', 'fox', 'fish']    
    words = max_match(sentence, dictionary)
    print(words)

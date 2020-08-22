#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
import numpy as np

class Ngram:
    
    def __init__(self, N):
        if type(N) == int and N > 0:
            self.N = N
        else:
            raise ValueError(f'{N} must be an positive integer..\n')
            
    def process(self, text):
        '''
        Erases the punctuation marks
        
        :param text: A text with punctuation marks
        :return: The text without punctuation marks
        '''
        text = text.lower()
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace(':', ' ')
        text = text.replace(';', ' ')
        text = text.replace('!', ' ')
        text = text.replace('?', ' ')
        new_text = text.replace('  ', ' ')
        while new_text != text:
            text = new_text
            new_text = text.replace('  ', ' ')
        text = new_text
        return text
            
        
    def split_text(self, text, sep=' '):
        '''
        Splits the text into words (default)
        Please change to "word_tokenize" if punctuation marks are important
        
        :param text: The text which is splitted into parts
        :param sep: Seperator string  (e.g. my name is -> ['my', 'name', 'is'])
        :return: List of word
        '''
    
        if sep == 'word_tokenize':
            wordlist = word_tokenize(text)
        else:
            text = self.process(text=text)
            wordlist = text.split(' ')
        while '' in wordlist:
            wordlist.remove('')
        return wordlist
        
    def __group_probability__(self, wordlist):
        '''
        Calculates the probability of N words phrases
        
        if N is 3, then
            calculate 3-word groups such as 'the red fox', 'red fox runs'.
        
        :param wordlist: List of text each word
        :return: 'the probabilities of wordtuple
        '''
        if self.N > len(wordlist):
            raise ValueError(f'{self.N} must be less than the length of wordlist {len(wordlist)}..\n')
            
        word_groups = [wordlist[i:i+self.N] for i in range(len(wordlist) - self.N + 1)]
        word_set = []
        for group in word_groups:
            if group not in word_set:
                word_set.append(group)
                
        prob_list = [(group, word_groups.count(group)/len(wordlist)) for group in word_set]        
        
        return prob_list

    def fit(self, text):
        '''
        Trains the text data and returns the probability list
        :param text: Text which is trained
        :return: The probability list
        '''
        
        new_text = self.process(text)
        wordlist = self.split_text(new_text)
        prob_list = self.__group_probability__(wordlist)
        
        return prob_list
        


text = 'Hello! My name is Buura. Did you understand what my name is?'
ng = Ngram(2)
print(ng.fit(text))
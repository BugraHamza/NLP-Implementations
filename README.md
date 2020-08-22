# NLP ALGORITHMS

My NLP algorithms and notes since my NLP journey started. 
- The notes are based one Dan Jurafsky's NLP Course [ https://www.youtube.com/playlist?list=PLLssT5z_DsK8HbD2sPcUIDfQ7zmBarMYv ]
(Notes haven't been uploaded yet.)

## The chosen and implemented algorithms:
    All implementations have comments and explanations in source code as well.

### 1) <a href="./implementations/Maximum Matching Algorithm/">Maximum Matching Algorithm</a>
    Maximum Matching Algorithm is an algorithm which finds the words of a sentence 
    if the sentence has no separators(spaces) between words. It is applicable for 
    languages such as Chinese, Japanese.
    It's not accurate for languages that have long words such as English.

### 2) <a href="./implementations/Porter's Algorithm/">Porter's Algorithm</a>
    Porter's Algorithm is an algorithm that is the most common English stemmer. 
    It finds the stem of the word. 
    (Note: The implementation does not include all the steps. May not be work for all words.)

### 3) <a href="./implementations/Binary Classifier/">Binary Classifier</a>
    Binary Classifier is a class of algorithms that look through the possible decisions and 
    decides the most possible one.
    The implementation is a binary classifier that decides whether a period ends a sentence or not.

### 4) <a href="./implementations/Minimum Edit Distance/">Minimum Edit Distance</a>
    Minimum Edit Distance is an algorithm which calculates the similarity between two words.
    Some of the applications of the algorithm are to correct the typos and recommend similar words. 
    There are various implementations (scoring systems) based on the task. The default scoring 
    system is Levenshtein.

### 5) <a href="./implementations/The Needleman-Wunsch Algorithm/">The Needleman-Wunsch Algorithm</a>
    The Needleman-Wunsch algorithm is an algorithm that maximizes the similarity 
    between two gene sequences (strings) to find the global alignment. All characters(nucleotides)
    must match.

### 6) <a href="./implementations/The Smith-Waterman Algorithm/">The Smşth-Waterman Algorithm</a>
    The Smith-Waterman algorithm is an algorithm that is used in NLP and Bioinformatics to detect 
    all possible alignments. Checking the confusion matrix is a way to find matches. 
    Some characters(nucleotides) may not match.

### 7) <a href="./implementations/Ngram/">Ngram (still working on it)</a>
    N-grams are a class of probabilistic language models that compute the probability of 
    a given word set or sentence. Its applications are, e.g., machine translation, 
    speech recognition,and so on. These algorithms use the chain rule of probability and 
    Markov assumption and use the formulas with a chosen N. Here, N stands for a positive 
    whole number. Some of most common N-gram models are unigrams(N=1), bigrams(N=2) and trigrams(N=3). 
    Unigrams computes the probability of a chosen word with Maximum Likelihood Estimate.
    Each model differs from each other in the size of word groups. Unigrams group the words 
    as themselves, bigrams as binary word groups, and trigrams as triple word groups.
 

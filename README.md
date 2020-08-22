# NLP ALGORITHMS

My NLP algorithms and notes since my NLP journey started. 
- The notes are based one Dan Jurafsky's NLP Course [ https://www.youtube.com/playlist?list=PLLssT5z_DsK8HbD2sPcUIDfQ7zmBarMYv ]
(Notes haven't been uploaded yet.)

## The chosen and implemented algorithms:
    All implementations have comments and explanations in source code as well.

### 1) Maximum Matching Algorithm
    Maximum Matching Algorithm is an algorithm which finds the words of a sentence. 
    If a sentence has no separators(spaces) between words. It is used for the languages 
    such as Chinese, Japanese.
    It' not accurate for the languages that has long words such as English.

### 2) Porter's Algorithm
    Porter's Algorithm is an algorithm that is the most common English stemmer.
    It finds the stem of word. 
    (Note: The implementation does not include all the steps. May not be work for all words.)

### 3) Binary Classifier
    Binary Classifier is a class of algorithms that ponder over the possible decisions and 
    decides the most possible one.
    The implementation is a binary classifier that decides whether a period ends a sentence or not.

### 4) Minimum Edit Distance
    Minimum Edit Distance is an algorithm which calculates the similarity between two words.
    The algorithm is used to correct the typos and recommend similar words. There are various 
    implementations (scoring systems) based on the task. Default scoring system is Levenshtein.

### 5) The Needleman - Wunsch Algorithm
    The Needleman - Wunsch Algorithm is an algorithm which maximizes the similarity between two
    gene sequences (strings) in order to find the global alignment. All characters(nucleotides)
    must match.

### 6) The Smith - Waterman Algorithm
    The Smith - Waterman Algorithm  is an algorithm which is used in NLP and Bioinformatics 
    in order to detect all possible alignments. A confusion matrix is used to check 
    which alignments are possible. Some characters(nucleotides) may not match.

### 7) Ngram (still working on it)
    N-grams are a class of probabilistic language models that compute the probabilty of 
    a given word set or sentence. Its applications are e.g. machine translation, speech recognition,
    and so on. This algorithms use basicly the chain rule of probability and Markov assumption and
    use the formulas with a chosen N. Here, N stands for a positive whole number. Some of most
    common N-gram models are unigrams(N=1), bigrams(N=2) and trigrams(N=3). 
    Unigrams computes the probability of a chosen word with Maximum Likelihood Estimate.
    Each model differs from each other in the size of word groups. Unigrams group the words 
    as themselves, bigrams as binary word groups, and trigrams as triple word groups.
 

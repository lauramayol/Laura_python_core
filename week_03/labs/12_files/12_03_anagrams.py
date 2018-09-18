'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
import anagram_sets


def store_anagrams(f1):
    #anagram_dict = dict()
    anagram_dict = anagram_sets.all_anagrams(f1)
    return anagram_dict


def read_anagrams(word, file_name):
    d = store_anagrams(file_name)
    word_key = anagram_sets.signature(word)
    return d[word_key]

print(read_anagrams("marble", "words.txt"))

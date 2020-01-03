from __future__ import unicode_literals
import nltk
import re

f = open ('baqarah.txt', encoding = 'utf-8').read()
f = f.replace('\ufeff','')
print (f)



class removeVowels():
    def __init__(self):
        self.re_short_vowels = re.compile(r'[\u064B-\u0652\u0670]')

    def removeSyakal (self, token):
        token = self.norm(token, 1)
        return token

    def norm(self, word, num=3):
        """
        normalization:
        num=1 normalize diacritics
        num=2 normalize initial hamza
        num=3 both 1&2
        """
        if num == 1:
            word = self.re_short_vowels.sub('',word)
        elif num == 2:
            word = word #self.re_initial_hamza.sub('\u0627', word)
        elif num == 3:
            word = self.re_short_vowels.sub('', word)
        return word
remove = removeVowels()
b = remove.removeSyakal(f)
print ('Hasil menghapus Syakal :' ,b)
print('----------------------------------------------------------------------')

t = nltk.word_tokenize(b)
print (t)

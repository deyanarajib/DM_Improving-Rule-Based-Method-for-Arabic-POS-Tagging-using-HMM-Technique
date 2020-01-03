import re, numpy as np
from nltk.stem.snowball import SnowballStemmer
import pyarabic.araby as araby
stemmer = SnowballStemmer('arabic')

buckwalter_map ={
		u"ا": "A", # alif
		u"ب": "b", # ba
                u"ة": "p", # ta marbuta
		u"ت": "t", # ta
		u"ث": "v", # tha
		u"ج": "j", # jim
		u"ح": "H", # Ḥa
		u"خ": "x", # kha
		u"د": "d", # dal
		u"ذ": "*", # dhal
		u"ر": "r", # ra
		u"ز": "z", # zin
		u"س": "s", # sin
		u"ش": "$", # shin
		u"ص": "S", # ṣad
		u"ض": "D", # Ḍad
		u"ط": "T", # Ṭa
		u"ظ": "Z", # Ẓa
		u"ع": "E", # 'Ayn
		u"غ": "g", # ghayn
		u"ف": "f", # fa
		u"ق": "q", # qaf
		u"ك": "k", # kaf
		u"ل": "l", # lam
		u"م": "m", # mim
		u"ن": "n", # nun
		u"ه": "h", # ha
		u"و": "w", # waw
		u"ي": "y", # ya
                
		#hamza
		u"ء": "'", # lone hamza
		u"أ": ">", # hamza on alif
		u"إ": "<", # hamza below alif
		u"ؤ": "&", # hamza on waw
		u"ئ": "}", # hamza on ya
                
		#alif
		u'ٓ' : "^",         # madda on alif
		u"ٱ": "{",         # alif alwasla
		u"\u0670": "`",    # dagger alif
		u"ى": "Y",         # alif maqsura
                
		#harakat
		u"\u064E": "a", # fatha
		u"\u064F": "u", # Damma
		u"\u0650": "i", # kasra
		u"\u064B": "F", # fathatayn
		u"\u064C": "N", # dammatayn
		u"\u064D": "K", # kasratayn
		u"\u0640": "_", # tatwil
                u"\u0652": "o", # sukun
                
		#others
		u"\u0651": "~", # shadda
                
}

harakat = '\u064E\u064F\u0650\u064B\u064C\u064D\u0652'

def remove_harakat(word):
    word = re.sub('['+harakat+']','',word)
    return word

def replace(char):
    return buckwalter_map[char]

with open('quran_simple.txt',encoding='utf-8') as f:
    data = f.read().splitlines()
    data = [remove_harakat(i.split('|')[-1]) for i in data]
f.close()

data = data[:100]

N = len(data)

for i in range(N):
    tokens = araby.tokenize(data[i])
    temp = []
    for word in tokens:
        temp.append((word,stemmer.stem(word)))
    data[i] = temp


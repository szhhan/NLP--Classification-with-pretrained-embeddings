#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:22:18 2019

@author: sizhenhan
"""

import re

class spell_check():
    
    def __init__(self, dic):
        self.dic = dic

    def words(self,text): 
        return re.findall(r'\w+', text.lower())

    def P(self,word): 
        return - self.dic.get(word, 0)

    def correction(self,word): 
        return max(self.candidates(word), key=self.P)

    def candidates(self,word): 
        return (self.known([word]) or self.known(self.edits1(word)) or [word])

    def known(self,words): 
        return set(w for w in words if w in self.dic)

    def edits1(self,word):
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self,word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def singlify(self,word):
        return "".join([letter for i,letter in enumerate(word) if i == 0 or letter != word[i-1]])
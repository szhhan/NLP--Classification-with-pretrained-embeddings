#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:26:41 2019

@author: sizhenhan
"""

import re
import emoji 
import unicodedata
import create_table

WORDS_REPLACER = [
    ("sh*t", "shit"),
    ("s**t", "shit"),
    ("f*ck", "fuck"),
    ("fu*k", "fuck"),
    ("f**k", "fuck"),
    ("f*****g", "fucking"),
    ("f***ing", "fucking"),
    ("f**king", "fucking"),
    ("p*ssy", "pussy"),
    ("p***y", "pussy"),
    ("pu**y", "pussy"),
    ("p*ss", "piss"),
    ("b*tch", "bitch"),
    ("bit*h", "bitch"),
    ("h*ll", "hell"),
    ("h**l", "hell"),
    ("cr*p", "crap"),
    ("d*mn", "damn"),
    ("stu*pid", "stupid"),
    ("st*pid", "stupid"),
    ("n*gger", "nigger"),
    ("n***ga", "nigger"),
    ("f*ggot", "faggot"),
    ("scr*w", "screw"),
    ("pr*ck", "prick"),
    ("g*d", "god"),
    ("s*x", "sex"),
    ("a*s", "ass"),
    ("a**hole", "asshole"),
    ("a***ole", "asshole"),
    ("a**", "ass"),
]

REGEX_REPLACER = []
for origin, new in WORDS_REPLACER:
    o1 = origin.replace("*", "\*")
    REGEX_REPLACER.append((re.compile(o1), new))
RE_SPACE = re.compile(r"\s")
RE_MULTI_SPACE = re.compile(r"\s+")


EMOJI_REGEXP = emoji.get_emoji_regexp()
UNICODE_EMOJI_MY = {}
for k, v in emoji.UNICODE_EMOJI_ALIAS.items():
    v = v.strip(':')
    v = v.replace('_', ' ')
    UNICODE_EMOJI_MY[k] = f" EMJ {v} "
    

def replace(match):
    return UNICODE_EMOJI_MY.get(match.group(0))

def my_demojize(string):
    return re.sub("\ufe0f", "", EMOJI_REGEXP.sub(replace, string))


TABLE = create_table.uncommon_char_table()

def normalize(text):
    text = my_demojize(text)
    text = RE_SPACE.sub(" ", text)
    text = unicodedata.normalize("NFKD", text)
    text = text.translate(TABLE)
    text = RE_MULTI_SPACE.sub(" ", text).strip()
    for pattern, repl in REGEX_REPLACER:
        text = pattern.sub(repl, text)

    return text
    
    
    
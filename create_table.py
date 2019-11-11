#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:05:24 2019

@author: sizhenhan
"""

import sys 
import unicodedata

def uncommon_char_table():
    CUSTOM_TABLE = str.maketrans(
            {
                    "\xad": None,
                    "\x7f": None,
                    "\ufeff": None,
                    "\u200b": None,
                    "\u200e": None,
                    "\u202a": None,
                    "\u202c": None,
                    "‘": "'",
                    "’": "'",
                    "`": "'",
                    "“": '"',
                    "”": '"',
                    "«": '"',
                    "»": '"',
                    "ɢ": "G",
                    "ɪ": "I",
                    "ɴ": "N",
                    "ʀ": "R",
                    "ʏ": "Y",
                    "ʙ": "B",
                    "ʜ": "H",
                    "ʟ": "L",
                    "ғ": "F",
                    "ᴀ": "A",
                    "ᴄ": "C",
                    "ᴅ": "D",
                    "ᴇ": "E",
                    "ᴊ": "J",
                    "ᴋ": "K",
                    "ᴍ": "M",
                    "Μ": "M",
                    "ᴏ": "O",
                    "ᴘ": "P",
                    "ᴛ": "T",
                    "ᴜ": "U",
                    "ᴡ": "W",
                    "ᴠ": "V",
                    "ĸ": "K",
                    "в": "B",
                    "м": "M",
                    "н": "H",
                    "т": "T",
                    "ѕ": "S",
                    "—": "-",
                    "–": "-",
                    }
            )


    invalid_lst = []
    for i in range(sys.maxunicode+1):
        if unicodedata.category(chr(i)) == "Mn":
            invalid_lst.append(i)
            NMS_TABLE = dict.fromkeys(ind for ind in invalid_lst)


    HEBREW_TABLE = {i: "א" for i in range(0x0590, 0x05FF)}
    ARABIC_TABLE = {i: "ا" for i in range(0x0600, 0x06FF)}
    CHINESE_TABLE = {i: "是" for i in range(0x4E00, 0x9FFF)}
    KANJI_TABLE = {i: "ッ" for i in range(0x2E80, 0x2FD5)}
    HIRAGANA_TABLE = {i: "ッ" for i in range(0x3041, 0x3096)}
    KATAKANA_TABLE = {i: "ッ" for i in range(0x30A0, 0x30FF)}
    
    
    TABLE = dict()
    TABLE.update(CUSTOM_TABLE)
    TABLE.update(NMS_TABLE)
    TABLE.update(CHINESE_TABLE)
    TABLE.update(HEBREW_TABLE)
    TABLE.update(ARABIC_TABLE)
    TABLE.update(HIRAGANA_TABLE)
    TABLE.update(KATAKANA_TABLE)
    TABLE.update(KANJI_TABLE)
    
    return TABLE 












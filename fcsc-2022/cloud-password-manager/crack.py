#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from werkzeug.security import check_password_hash
from multiprocessing import Process

chars = "hkmquGIOST24"

# Function which test if hash and password are corresponding
def test(pass_to_test):
    if check_password_hash("sha256$FKM5MLhBFZ87pPgI$a51c4c0463d199fcf4a18bd8df2f40360c46e9caed05072618e8026f02dc83bf", pass_to_test):
        print(f"[\x1b[92m+\x1b[0m] Password found: '{pass_to_test}'!")
        exit()

# Generate all permutations of chars
def permutations(start, end=[]):
    if len(start) == 0:
        res = "".join(end)
        test(res)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])


print(f"[\x1b[92m+\x1b[0m] Starting bruteforce...")

for i in range(1, 13):
    # Generate all strings with differents first char
    res = chars[-i:] + chars[:-i]

    print(f"[\x1b[94m>\x1b[0m] Creating thread for those chars: {res}")
    
    # Create thread which executes 'permutations' function with strings generated
    add = Process(target=permutations, args=(list(res),))

    # Start thread
    add.start()
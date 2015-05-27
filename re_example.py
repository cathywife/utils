#!/usr/bin/python


import re


if __name__ == "__main__":
    print re.sub("\d+", "11", "10 20 30 40 50")

    print re.sub("\d+", lambda m: str(int(m.group(0)) * 2), "10 20 30 40 50")
    print re.sub("\w+", lambda m: m.group(0) + "ing", "laugh eat sleep think")
    print re.subn("\d+", lambda m: str(int(m.group(0)) * 2) , "1 2 3 4 5")


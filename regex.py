import re

# Compilation Flags:
#   ASCII - A       -   Match only ASCII characters
#   DOTALL - S      -   Make . match any character (including newlines)
#   IGNORECASE - I  -   Case-insensitive matches
#   LOCALE - L      -   Locale-aware match (match based on locale label)
#   MULTILINE - M   -   Multi-line matching (affects ^ and $)
#   VERBOSE - X     -   'extended' - Allows for things like comments in compile

def matchVal(str, comp):
    m = comp.match(str)
    if(m):
        return m
    else:
        return None

def findList(str, comp):
    list = comp.findall(str)     # find all instances and return as a list

    if(list):
        return list
    else:
        return None
    
def iteration(str, comp):
    iter = comp.finditer(str)       # find all instances and return as a sequence of match object instances as an iterator

    if(iter):
        return iter
    else:
        return None

def menu():
    # separate each sequence of outputs to make it easier to read/define
    separator = ("~"*50)
    basicString = "This is a basic bassic string to test thee the RegEx in Python3. Numbers will also be tested. So 1, 2, ... n many numbers will be tested as well."
    
    print(separator, "\nTesting String\n", basicString)

    # basic compiler tests
    a = re.compile(r"(test)+")      # match 1 or more times     -   equivalent to {1,}
    b = re.compile(r"bas*ic", re.I)       # match 0 or more times     -   equivalent to {0,}
    c = re.compile(r"\d")           # match any decimal digit   -   equivalent to [0-9]
    d = re.compile(r"the?")       # match 0 or 1 times        -   equivalent to {0,1}
    e = re.compile("[a-z]+")           # match all lowercase letters    -   equivalent to [abcdefghijklmnopqrstuvwxyz]
    f = re.compile("this", re.I)           # match 'this' regardless of upper/lower case

    # Put all compiled RegEx meant to be printed as lists in a single list
    compiledForLists = []
    compiledForLists.append(a)
    compiledForLists.append(b)
    compiledForLists.append(c)
    compiledForLists.append(d)
    compiledForLists.append(e)

    # Put all compiled RegEx meant to find matches in a single list
    compiledForMatches = []
    compiledForMatches.append(f)

    # findall
    print(separator, "\nPrinting lists")
    count = 1
    for i in compiledForLists:
        print(count, ":", findList(basicString, i))
        count += 1

    print(separator + "\nPrinting match cases")
    count = 1
    for i in compiledForMatches:
        print(count, ":", matchVal(basicString, i))
        count += 1

menu()




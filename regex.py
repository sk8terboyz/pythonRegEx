import re

# Compilation Flags:
#   ASCII - A       -   Match only ASCII characters
#   DOTALL - S      -   Make . match any character (including newlines)
#   IGNORECASE - I  -   Case-insensitive matches
#   LOCALE - L      -   Locale-aware match (match based on locale label)
#   MULTILINE - M   -   Multi-line matching (affects ^ and $)
#   VERBOSE - X     -   'extended' - Allows for things like comments in compile

def menu():
    # separate each sequence of outputs to make it easier to read/define
    separator = ("~"*50)
    basicString = "This is a basic bassic string to test thee the RegEx in Python3. Numbers will also be tested. So 1, 2, ... n many numbers will be tested as well."
    emails = "test.tester@hotmail.com alphabeov none of this should be matched person@ilstu.edu Tet-est_@gmail.com gov.g.o.v@edu.gov"
    print(separator, "\nTesting String\n", emails)

    def compileBasic(comp):
        # basic compiler tests
        a = re.compile(r"(test)+")      # match 1 or more times     -   equivalent to {1,}
        b = re.compile(r"bas*ic", re.I)       # match 0 or more times     -   equivalent to {0,}
        c = re.compile(r"\d")           # match any decimal digit   -   equivalent to [0-9]
        d = re.compile(r"the?")       # match 0 or 1 times        -   equivalent to {0,1}
        e = re.compile("[a-z]+")           # match all lowercase letters    -   equivalent to [abcdefghijklmnopqrstuvwxyz]
        f = re.compile("this", re.I)           # match 'this' regardless of upper/lower case
        g = re.compile(r"[\w]+")         # all alphanumeric values   -   equivalent to [a-zA-Z0-9_] - without the '+' it would do by character instead of word
        comp.append(a)
        comp.append(b)
        comp.append(c)
        comp.append(d)
        comp.append(e)
        comp.append(f)
        comp.append(g)
        return comp

    def compileForEmails(comp):
        email = re.compile(r"^[\w\$\_]?[\w\$\-\_\.]*@([\w\-]*\.)+[\w]+")
        comp.append(email)
        return comp

    # Put all compiled RegEx meant to be printed as lists in a single list
    def findAllBasics(comp):
        basics = compileBasic(comp)
        for b in basics:
            print(b.findall(basicString))
    
    def checkEmails(comp):
        emailCheck = compileForEmails(comp)
        for e in emailCheck:
            print((e.match(emails)))
    
    # compiled = []
    # findAllBasics(compiled)
    compiled = []
    checkEmails(compiled)

menu()




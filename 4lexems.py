def lexem(lex):
    """Search of lexems in text"""
    pass
    import re
    text = open('text.txt', 'r')
    txt = text.read()         
    spisok = []
#changing registr of lexem  
    up = txt.lower()
#making lexem without signs of punctuation
    n = len(lex)
    lexs = lex[0:n]
#search of lexems in text
    res = re.finditer(lexs, up)
    for match in res:
        spisok.append(match.group())
    dlina = len(spisok)
    text.close()    
    return {lex : dlina}

print "Here we go again, choose your lexem ",lexem(raw_input())

if __name__ == "__main__":
    import doctest
    doctest.testmod()

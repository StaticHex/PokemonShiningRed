"""
================================================================================
FORMATTING CONSTANTS
================================================================================
"""

LEFT = 0
RIGHT = 1
CENTER = 2


def printWrapped(string, length, offset, lead="", trail=""):
    str_len = len(string)
    l_len = len(lead)
    t_len = len(trail)
    cor_len = length - l_len - t_len
    i = 0
    tok = ""
    while(i < str_len):
        tok += string[i]
        if(len(tok) > cor_len):
            while(tok[-1] != " "):
                tok = tok[:-1]
                i -= 1
            tok = tok[:-1]
            print lead+padString(tok,cor_len,LEFT)+trail
            tok = " "*offset
        i += 1
    print lead+padString(tok,cor_len,LEFT)+trail

def writeWrapped(f,string, length, offset, lead="", trail=""):
    str_len = len(string)
    l_len = len(lead)
    t_len = len(trail)
    cor_len = length - l_len - t_len
    i = 0
    tok = ""
    while(i < str_len):
        tok += string[i]
        if(len(tok) > cor_len):
            while(tok[-1] != " "):
                tok = tok[:-1]
                i -= 1
            tok = tok[:-1]
            f.write(lead+padString(tok,cor_len,LEFT)+trail+"\n")
            tok = " "*offset
        i += 1
    f.write(lead+padString(tok,cor_len,LEFT)+trail+"\n")

def padString(string, length, style):
    i = 0
    while(len(string) < length):
        if style is 0:
            string += " "
        elif style is 1:
            string = " "+string
        else:
            if i % 2 is 0:
                string += " "
            else:
                string = " "+string
            i += 1
    return string

def inchToFt(inches):
    feet = 0
    return str(inches / 12)+"' "+str(inches % 12)+"\""

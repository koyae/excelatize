import re

def excelify(string):
    lines = string.split("\n")
    newlines = []
    for x in range(0,len(lines)):
        newlines.append("")
        quotedIn = False
        runLen = 0 # number of characters in the current quoted string
        for y in range(0,len(lines[x])):
            if lines[x][y] != "\t":
                if not quotedIn:
                    newlines[x] += "& " if x!=0 else ""
                    newlines[x] += '"'
                    quotedIn = True
                else:
                    if runLen>=255:
                        newlines[x] += '" & "'
                        runLen = 0
                newlines[x] += lines[x][y] if lines[x][y]!='"' else '""'
                runLen += 1
            else:
                if quotedIn:
                    newlines[x] += '"'
                    quotedIn = False
                    runLen = 0
                newlines[x] += "& CHAR(9) &"
        if quotedIn:
            newlines[x] += '"'
        newlines[x] += " & CHAR(10)"
    newlines = "\n".join(newlines)
    newlines = "= " + newlines
    newlines = newlines.replace("&&","&")
    print newlines

#!/opt/python-2.7/bin/python2.7 -S
#  -*- coding: utf-8 -*-

# Script to copy standard input to standard output, one line at a time.


# This gets various items to interfaces with the OS, including the
# standard input stream.
import sys

# This is apparently for Python rogues, but I got it from SO and it seems to work.
# http://stackoverflow.com/questions/11741574/how-to-set-the-default-encoding-to-utf-8-in-python
# A key trick is the -S business above in the shebang line.
# sys.setdefaultencoding("UTF-8")
# # print sys.getdefaultencoding()
import site

V1 = u"\u0E40\u0E41\u0E42\u0E43\u0E44"
C1 = u"\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D\u0E0E\u0E0F" \
     + u"\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F" \
     + u"\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E"
C2 = u"\u0E23\u0E25\u0E27\u0E19\u0E21"
V2 = u"\u0E34\u0E35\u0E36\u0E37\u0E38\u0E39\u0E31\u0E47"
T  = u"\u0E48\u0E49\u0E4A\u0E4B"
V3 = u"\u0E32\u0E2D\u0E22\u0E27"
C3 = u"\u0E07\u0E19\u0E21\u0E14\u0E1A\u0E01\u0E22\u0E27"

#print(V1)
# print C1
# print C2
# print V2
# print T
# print V3
# print C3

# print V1 + C1 + C2

def fst(I):
    # Transform the input to the result
    # A dummy line to prove stringy things work with Unicode.
    # return u":"+ I

    state = 0
    myresult = u""
    for x in I:
        if state == 0:
            if x in V1:
                state = 1
                myresult += x
            elif x in C1:
                state = 2
                myresult += x
        elif state == 1:
            if x in C1:
                state = 2
                myresult += x
        elif state == 2:
            if x in C2:
                state = 3
                myresult += x
            elif x in V2:
                state = 4
                myresult += x
            elif x in T:
                state = 5
                myresult += x
            elif x in V3:
                state = 6
                myresult += x
            elif x in C3:
                state = 9
                myresult += x + u" "
            elif x in V1:
                state = 7
                myresult += u" " + x
            elif x in C1:
                state = 8
                myresult += u" " + x
        elif state == 3:
            if x in V2:
                state = 4
                myresult += x
            elif x in T:
                state = 5
                myresult += x
            elif x in V3:
                state = 6
                myresult += x
            elif x in C3:
                state = 9
                myresult += x + u" "
        elif state == 4:
            if x in T:
                state = 5
                myresult += x
            elif x in V3:
                state = 6
                myresult += x
            elif x in C3:
                state = 9
                myresult += x + u" "
            elif x in V1:
                state = 7
                myresult += u" " + x
            elif x in C1:
                state = 8
                myresult += u" " + x
        elif state == 5:
            if x in V3:
                state = 6
                myresult += x
            elif x in C3:
                state = 9
                myresult += x + u" "
            elif x in V1:
                state = 7
                myresult += u" " + x
            elif x in C1:
                state = 8
                myresult += u" " + x
        elif state == 6:
            if x in C3:
                state = 9
                myresult += x + u" "
            elif x in V1:
                state = 7
                myresult += u" " + x
            elif x in C1:
                state = 8
                myresult += u" " + x

        if state == 7:
            #myresult += str(state)
            state = 1
        elif state == 8:
            #myresult += str(state)
            state = 2
        elif state == 9:
            #myresult += str(state)
            state = 0
        #myresult += str(state)
    return myresult

print(u"<html><meta http-equiv='Content-Type' content='text/html; charset=UTF-8' /><body>")

writefile = open("kekoar.html", "w+", encoding="utf-8")
writefile.write(u"<html>\n<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />\n<body>\n")

# # Readline is a method of stdin, which is in the standard object sys.
# # It returns the empty string on EOF.
# line = sys.stdin.readline()

readfile = open("/opt/dropbox/17-18/473/project3/fsm-input.utf8.txt", 'r', encoding="utf-8")
text = readfile.readlines()


# The string line works as the while test.  As several other scripting
# languages, the empty string is treated as false, other strings are treated
# as true.
for line in text:
    # Transform the line read.  Since readline leaves the terminating newline,
    # a slice is used to print all characters in the string but the last.
    # Otherwise, each input line would be output with two line terminators.
    result = fst(line[:-1])

    # print(result + u"<br/>")
    writefile.write(result + u"<br/>\n")

print(u"</body></html>")
writefile.write(u"</body>\n</html>")

# # Project 3
# This script reads a controlled Thai text and prints out a copy
# of the text if it matches a set of rules defined by a FSM
# The FSM is implemented in a series of if then statements because
# I could not figure out how to switch in python and I am not very good
# with classes

# Defining the acceptable inputs for transitions
V1 = u"\u0E40\u0E41\u0E42\u0E43\u0E44"
C1 = u"\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D\u0E0E\u0E0F" \
     + u"\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F" \
     + u"\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E"
C2 = u"\u0E23\u0E25\u0E27\u0E19\u0E21"
V2 = u"\u0E34\u0E35\u0E36\u0E37\u0E38\u0E39\u0E31\u0E47"
T  = u"\u0E48\u0E49\u0E4A\u0E4B"
V3 = u"\u0E32\u0E2D\u0E22\u0E27"
C3 = u"\u0E07\u0E19\u0E21\u0E14\u0E1A\u0E01\u0E22\u0E27"

# The FSM
def fst(I):

    state = 0 # sets the state to zero for each line (only one line is sent to function at a time

    myresult = u"" # cat string of acceptable output
    for x in I: # for character in the string
        if state == 0: # If currently in state 0, and acceptable inputs for zero state
            if x in V1:
                state = 1
                myresult += x
            elif x in C1:
                state = 2
                myresult += x
        elif state == 1:    # inputs for state 1
            if x in C1:
                state = 2
                myresult += x
        elif state == 2: # inputs for state 2
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
        elif state == 3: # inputs for state 3
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
        elif state == 4: # inputs for state 4
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
        elif state == 5: # inputs for state 5
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
        elif state == 6: # inputs for state 6
            if x in C3:
                state = 9
                myresult += x + u" "
            elif x in V1:
                state = 7
                myresult += u" " + x
            elif x in C1:
                state = 8
                myresult += u" " + x

# Accept states, change state back to 1, 2, or 3
        if state == 7:
            state = 1
        elif state == 8:
            state = 2
        elif state == 9:
            state = 0
    return myresult

# output file
writefile = open("kekoar.html", "w+", encoding="utf-8")
# header of output file
writefile.write(u"<html>\n<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />\n<body>\n")

# Source file
readfile = open("/opt/dropbox/17-18/473/project3/fsm-input.utf8.txt", 'r', encoding="utf-8")
text = readfile.readlines()

for line in text:
    result = fst(line[:-1])

    writefile.write(result + u"<br/>\n")

writefile.write(u"</body>\n</html>")

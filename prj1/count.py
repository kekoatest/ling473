import re       # import regex

tcon = 0        # total counter
scon = 0        # total s counter
npcon = 0       # total np counter
vpcon = 0       # total vp counter
ditracon = 0        # total ditra counter
intracon = 0        # total intra counter

stats = []      # array for holding stats for fact checking
stats2 = []     # another array for computer-readable fact checking

i = 0   # 10s place
j = 0   # 1s place

while i < 10:
    j = 0
    while j < 10:

        doc = "wsj_14" + str(i) + str(j) + ".prd"
        # print(doc)       # print current file
        filename = "/corpora/LDC/LDC99T42/RAW/parsed/prd/wsj/14/" + doc
        fileopen = open(filename)
        text = fileopen.read()
        fileopen.close()

        nodes = []      # list of all counted constituents (list type list [const type and counter for ditransitives]
        nodes.append(["BLANK",0])   # placeholder
        con = 0         # counter for list of words (always set to to index)
        scount = 0      # s counter
        npcount = 0     # np counter
        vpcount = 0     # vp counter
        ditracount = 0  # ditransitive counter
        intracount = 0  # intransitive counter

        count = 0       # the character in the text
        text = re.sub("\r", "", text)       # Remove carriage
        text = re.sub("\n", "", text)       # Removenew line
        text = re.sub("\s+", " ", text)     # Remove double spaces
        for ch in text:
            if ch == "(":
                if text[count+1] == "S" and text[count+2] == " ":
                    nodes.append(["S", 0])
                    scount += 1
                    con += 1
                elif text[count+2] == "S" and text[count+3] == " ":
                    nodes.append(["S", 0])
                    scount += 1
                    con += 1
                elif text[count+1] == "N" and text[count+2] == "P" and (text[count+3] == " " or text[count+3] =="("):
                    nodes.append(["NP", 0])
                    npcount += 1
                    con += 1
                elif text[count+2] == "N" and text[count+3] == "P" and (text[count+4] == " " or text[count+4] =="("):
                    nodes.append(["NP", 0])
                    npcount += 1
                    con += 1
                elif text[count+1] == "V" and text[count+2] == "P" and (text[count+3] == " " or text[count+3] =="("):
                    nodes.append(["VP", 0 ,0])
                    vpcount += 1
                    con += 1
                elif text[count+2] == "V" and text[count+3] == "P" and (text[count+4] == " " or text[count+4] =="("):
                    nodes.append(["VP", 0, 0])
                    vpcount += 1
                    con += 1
                else:
                    nodes.append(["NOTMARKED",0])
                    con += 1
            elif ch == ")":
                temp = nodes.pop()
                if nodes[con-1][0] == "VP":
                    if temp[0] == "NP":
                        nodes[con-1][1] += 1
                        nodes[con-1][2] += 1
                    else:
                        nodes[con-1][2] += 1

                if temp[0] == "VP":
                    if temp[1] == 2:
                        ditracount += 1
                    elif temp[2] == 0:
                        intracount += 1

                con -= 1

            count += 1

        # Block comments are for writting ind file stats
        # report = doc \
        #     + "\nS:\t\t" + str(scount) \
        #     + "\nNP:\t\t" + str(npcount) \
        #     + "\nVP:\t\t" + str(vpcount) \
        #     + "\nDVP:\t\t" + str(ditracount) \
        #     + "\nIVP:\t\t" + str(intracount) \
        #     + "\n\n"
        #
        # report2 = doc \
        #     + "\tS:\t" + str(scount) \
        #     + "\tNP:\t" + str(npcount) \
        #     + "\tVP:\t" + str(vpcount) \
        #     + "\tDVP:\t" + str(ditracount) \
        #     + "\tIVP:\t" + str(intracount) \
        #     + "\n"
        #
        # stats.append(report)
        # stats2.append(report2)

        scon += scount
        npcon += npcount
        vpcon += vpcount
        ditracon += ditracount
        intracon += intracount

        j += 1

    i += 1

# fileopen = open("stats.txt", "w+")
# for item in stats:
#     fileopen.write(item)
# fileopen.close()
#
# fileopen = open("rythmetic.txt", "w+")
# for item in stats2:
#     fileopen.write(item)
# fileopen.close()

print("Constituent Counts:")
print("\nS:\t" + str(scon))
print("NP:\t" + str(npcon))
print("VP:\t" + str(vpcon))
print("DITRA:\t" + str(ditracon))
print("INTRA:\t" + str(intracon))

print("\nFINISH")

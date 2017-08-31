resource = open("/opt/dropbox/17-18/473/project4/targets")
targets = resource.readlines()

writefile = open("targs.txt", "w+")

for line in targets:
    writefile.write(line + "\n")

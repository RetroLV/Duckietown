fh = open("Heyo.txt", "w")
fh.write("Hey guys!\n")
fh.close()
fh = open("Heyo.txt", "r")
print(fh.read())
fh.close()
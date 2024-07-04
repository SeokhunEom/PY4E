fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    str = line.rstrip().lower()
    if str.startswith('from') and str.startswith('from:') == False:
        count += 1
        words = str.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")

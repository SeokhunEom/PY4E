name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}

for line in handle:
    str = line.rstrip()
    if str.startswith("From"):
        words = str.split()
        if len(words) > 2:
            hms = words[5]
            h = hms[:2]
            dict[h] = dict.get(h,0) + 1

arr = list()
for k, v in dict.items() :
    tmp = (k, v)
    arr.append(tmp)

arr.sort()

for a, b in arr:
    print(f"{a} {b}")

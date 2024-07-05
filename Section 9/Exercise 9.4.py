name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = {}
max_num = 0;
max_name = ""

for line in handle:
    str = line.rstrip()
    if str.startswith("From"):
        words = str.split()
        name = words[1]
        if name in dict.keys():
            dict[name] += 1
        else:
            dict[name] = 1


for key in dict:
    if dict[key] > max_num:
        max_num = dict[key]
        max_name = key

print(f"{max_name} {int(max_num/2)}")

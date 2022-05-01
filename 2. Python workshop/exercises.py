from pprint import pprint
import os, sys

transmissions = []
with open(os.path.join(sys.path[0], "transmissions.csv")) as file:
    for line in file:
        line = line.strip()
        transmissions.append(line.split(","))
pprint(transmissions)
print("\n")

transmissions.pop(0)
ids = [row[0] for row in transmissions]
transmissions = [row[1] for row in transmissions]
sums = []
for t in transmissions:
    current_sum = 0
    for char in t:
        try:
            current_sum += int(char)
        except:
            continue
    sums.append(current_sum)
print(sums)
print("\n")

dict = {int(ids[i]):sums[i] for i in range(len(ids))}
dict_sorted = sorted(dict.items())
message = ""
for item in dict_sorted:
    message += chr(item[1])
print(message)
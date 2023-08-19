#sample = input().strip("(").strip(")")
sample = "S".split("(") 
print(sample)

for i, line in enumerate(sample):
    lists = line.split(")")
    sample[i] = lists[0]
    del lists[0]
    for thing in lists:
        sample.append(thing)

output = ""
counts = {"S": 0, "T": 0, "R": 0, "L": 0}
multiplier = 1

for line in sample:
    for _ in range(multiplier):
        multiplier = 1
        current_multi = ""
        for i, char in enumerate(line):
            if char.isdigit() and i != len(line) - 1: # Is digit and not last in index
                current_multi += char
            elif char.isdigit(): # Index and last in index
                current_multi += char
                multiplier = int(current_multi)
            else: # Not a digit
                if not current_multi:
                    current_multi = "1"
                counts[char] += 1 * int(current_multi)
                output += char * int(current_multi)
                current_multi = ""

print(output)

values = list(counts.values())
values = [str(x) for x in values]

print(" ".join(values))
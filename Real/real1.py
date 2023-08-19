names_order = input().split(" ")

lines = int(input())

data = []
for _ in range(lines):
    data.append(input())

swap_instructions = []

# Start at index 1 of data, end at last index of data
for i in range(len(data)):
    instructions = [int(num) for num in data[i].split(" ")]
    swap_instructions.append(instructions)

for instruction in swap_instructions:
    names_order[instruction[0] - 1], names_order[instruction[1] - 1] = names_order[instruction[1] - 1], names_order[instruction[0] - 1]

print(" ".join(names_order))
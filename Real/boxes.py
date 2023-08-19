
data = "1 1 2 2 2 3"

sample = data.split(" ")
sample.sort()
sample.reverse()

boxes = []
counts = {}

for digit in sample:
    try:
        counts[digit] += 1
    except Exception:
        counts[digit] = 1

avalable_numbers = list(counts.keys())

while avalable_numbers:
    box = []
    for digit in avalable_numbers:
        box.append(digit)
        counts[digit] -= 1
        if counts[digit] <= 0:
            del counts[digit]

    boxes.append(box)
    avalable_numbers = list(counts.keys())

#for unit in boxes:
#    lowest_length = 99999
#    for i, length in enumerate(unit):
#        if int(length) < int(lowest_length):
#            lowest_length = length
#    for unit in reversed(boxes):
#        if not lowest_length in unit:


boxes.sort()
boxes.reverse()

for unit in boxes:
    smallest_unit_layer = len(boxes)

import sys
sys.exit()

for box in boxes:
    box = [str(x) for x in box]

    print(" ".join(box).strip())
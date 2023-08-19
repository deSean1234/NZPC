import math, sys

#start_and_end_values = input().split(" ")
start_and_end_values = "-3 3".split(" ")

start_value = int(start_and_end_values[0])
end_value = int(start_and_end_values[1])

if start_value > 0 or end_value < 0 or end_value == start_value:
    print(0)
    sys.exit()

#devider_heights = input().split(" ")
devider_heights = "3 3 3 3".split(" ")

devider_heights = [int(n) for n in devider_heights]

left = []
right = []

left_count = math.floor(start_value * -1/2 + 1)

for _ in range(left_count):
    left.append(devider_heights[0])
    del devider_heights[0]

right = devider_heights
left.reverse()

try:
    while left[0] == right[0]:
        left[0] += left[1] * 2
        del left[1]
        right[0] += right[1] * 2
        del right[1]
except Exception:
    pass

if left[0] > right[0]:
    side = right
else:
    side = left

total_volume = 0

for devider in side:
    total_volume += 2 * devider

#print(left)
#print(right)
print(int(total_volume))
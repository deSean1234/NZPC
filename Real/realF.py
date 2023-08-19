vote_numbers = int(input())
winning_num = 0

winners = []
votes = {}

for _ in range(vote_numbers):
    name = input()
    try:
        votes[name] += 1
    except Exception:
        votes[name] = 1

for name, value in votes.items():
    if value > winning_num:
        winning_num = value
        winners = [name]
    elif value == winning_num:
        winners.append(name)

numbers = list(votes.values())
numbers.append(0)
numbers.remove(winning_num)
numbers.sort()
numbers.reverse()

winners.sort()

if len(winners) > 1:
    print("Tie between ", end="")
    for i, name in enumerate(winners):
        if i < len(winners) - 1:
            print(f"{name}, ", end="")
        else:
            print(f"{name}", end="")
    print(".")
else:
    if winning_num - numbers[0] != 1:
        do_s = "s"
    else:
        do_s = ""
    print(f"{winners[0]} won by {winning_num - numbers[0]} vote{do_s}.")

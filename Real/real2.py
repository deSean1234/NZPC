import sys

def doubles(roll):
    roll = roll.split(" ")
    if roll[0] == roll[1]:
        print(f"Doubles. Move forwards {int(roll[0]) + int(roll[1])} squares.")
        sys.exit()

roll_one = input()
doubles(roll_one)
roll_two = input()
doubles(roll_two)
roll_three = input()
doubles(roll_three)

card = input()

roll_three = roll_three.split(" ")

if card == "y":
    print(f"Use card. Move forwards {int(roll_three[0]) + int(roll_three[1])} squares.")
else:
    print(f"$50 fine. Move forwards {int(roll_three[0]) + int(roll_three[1])} squares.")



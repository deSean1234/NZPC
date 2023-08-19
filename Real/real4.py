word_to_guess = input().upper()

letters = []
total_guess = 0
given_up = False
guess_count = 0
results = []

guessing = True
while guessing:
    i = 0
    cow = 0
    bull = 0
    cow_plural = "cows"
    bull_plural = "cows"
    user_guess = input().upper()

    guess_count += 1

    # if user has given up
    if user_guess == "GIVE UP":
        given_up = True
        break
    
    for letter in user_guess.split():
        if user_guess[i] == user_guess[i+1]:
            continue
        elif user_guess[i] != user_guess[i+1]:
            letters.append(letter)
        i += 1

        
    for i in range(len(letters)):
        if letters[i] == word_to_guess[i]:
            bull += 1
            continue
        elif letters[i] in word_to_guess:
            cow += 1
            continue

    
    if bull == 1:
        bull_plural = "bull"
    else:
        bull_plural = "bulls"

    if cow == 1:
        cow_plural = "cow"
    else:
        cow_plural = "cows"
    
    
    results.append(f"{user_guess} Score {bull} {bull_plural} and {cow} {cow_plural}.")

    if user_guess == word_to_guess:
        break

for i in range(len(results)):
    print(results[i])

if given_up:
    print(F"The word was not guessed. Answer: {word_to_guess}.")
else: print(f"The word was guessed in {guess_count}.")

    
word = ""
guess_word = "python"
guess_limit = 3
guess_count = 0
guess_max = False

while word != guess_word and not(guess_max):
    if guess_count < guess_limit:
        word = input("guess the word: ")
        guess_count += 1
    else:
        guess_max = True

if guess_max:
    print("you lose!")
else:
    print("you win!")

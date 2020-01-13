secret_word = "Maurice"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
print("The limit is 3 guesses !")

while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter secret word :")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Sorry, time out !")
else:
    print("Congratulation, You won !")
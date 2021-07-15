import random

incorrect_guess = []
answer = []
user_guess = []
lives = 10


#This chooses a random word
def random_line(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)
secret = random_line('word_list.txt')
#print(secret)


#This assembles the user_guess list
for i in range(len(secret)):
    user_guess.append('_')


#THis function is how we find where the guessed letters are in the word
def read(letter, string):
    places = []
    for i in range(len(string)):
        if(string[i] == letter):  
            places.append(i)
    return places


#This makes the string a list to compare to the user guess
for i in secret:
    answer.append(i)


#This puts the correctly guessed letters into the user_guess list in the right places
print(user_guess)
while lives > 0 and user_guess != answer:
    guess = input('guess a letter: ').lower().strip()
    if guess in user_guess:
        print('you already guessed that silly')
    elif guess in secret:
        for i in read(guess, secret):
            user_guess[i] = guess
        print(user_guess)
    elif guess not in secret:
        lives = lives-1
        incorrect_guess.append(guess)
        print('lives: ' + str(lives) + '\nincorrect guesses: ' + str(incorrect_guess))


#This spits out wether or not the player won the game
if user_guess == answer:
    print('You win!')
    print(secret)
elif user_guess != answer:
    print('you lose')
    print('the word was: ' + secret)




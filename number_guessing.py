import random
limit = input('Set the upper bound for the number guessing game: ')
answer = random.randint(0, int(limit))
x = 0

while True:
    guess = input("Guess a number: ")
    guess = int(guess)
    if guess == answer: break
    elif guess > answer: 
        print("too high\n") 
        x+=1
    elif guess < answer: 
        print("too low\n") 
        x+=1
print("you win \nscore: " + str(x))



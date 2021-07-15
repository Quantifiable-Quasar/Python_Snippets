"""
Flashcard script that allows for a variable number of facts on the back of the card
"""

import random

# This is the dictionary of prebuilt flashcards that the user studies

study_set = {

}

# User chooses what text file to open and read to generate the study_set dictionary

to_study = input('what to study ')
file = open(to_study)

"""
For loop takes line from text file and inputs it into dictionary
It splits the words by comma
The first line of the text file must have all the questions 

For example if you want the user to input the atomic number and abbreviation for an element the first line should be:
abbreviation atomic_number
"""
x = 0
for i in file:
    # Converts one line of text from the file and makes it a dictionary entry
    i = i.split()
    # Takes the first word as the name of the entry and all the following as the definition
    j = i[0]
    del i[0]
    # Checks to make sure that the entry appended isn't the first line so it adds information not arguments
    if x > 0: study_set[j] = i
    x += 1
file.close()
"""
main game loop
"""

while True:
    # Selects a random line from the text file / dictionary entry and turns it into a flashcard
    flashcard = random.choice(list(study_set))
    # takes the first line of the text file which are where the number of questions is declared
    arguments = open(to_study).readline()
    arguments = arguments.split()
    # Gives the user the question
    print(flashcard)
    user_answers = []
    # Asks for user input and stores that in a list
    for i in range(len(arguments)):
        user_answers.append(input(arguments[i] + ': '))
    # Checks if that list is equal to the dictionary entry and then returns win or lose
    if user_answers == study_set[flashcard]:
        print('correct')
    elif user_answers != study_set[flashcard]:
        print('incorrect answer was ' + str(study_set[flashcard]))

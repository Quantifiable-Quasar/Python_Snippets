#Reverse string by character

string = input("String to reverse: ")
list = []
reversed = []
final_string = ""
space = " "
for letter in string:
    list.append(letter)

for x in range(0, len(list)):
    reversed.append(list[-1])
    del list[-1]

for element in reversed:
    final_string = final_string + element
print(final_string)



#Reverse sentence by word

sentence = input("Sentence to reverse by word: ")
reversed = []
list = sentence.split()
final_sentence = ""

#Reverse the list
for x in range(0, len(list)):
    reversed.append(list[-1])
    del list[-1]

#Reassembles the string from the list
for word in reversed:
    final_sentence = final_sentence + word + space 
print(final_sentence)



#Reverse every word by letter in sentence
sentence = input("Sentence to wangjangle: ")
list = sentence.split()
reversed = []
temp_list = []
temp_reversed = []
final_sentence = ""

#first loop runs through every word on the list
for x in range(0, len(list)):
    temp_word = list[x]
#next two loops reverse the word
    for letter in temp_word:
        temp_list.append(letter)
    temp_reversed = []
    for i in range(0, len(temp_list)):
        temp_reversed.append(temp_list[-1])
        del temp_list[-1]
    final_string = ''
#adds the reversed words back into a list
    for letter in temp_reversed: final_string = final_string + letter
    reversed.append(final_string)
#turns the final list of reversed words into a string
for word in reversed: 
    final_sentence = final_sentence + word + space
print(final_sentence)




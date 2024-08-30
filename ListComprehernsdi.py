prev_list = [-1,10,-20,2,-90,32,12,20]

new_list = [number for number in prev_list if number < 0 ]
print(new_list)


sentence = "I am a sentence"


def is_consonant(letter):
    letter = letter.lower()
    return letter not in 'aeiou '


new_sentence = [letter for letter in sentence if is_consonant(letter)]

print(new_sentence)
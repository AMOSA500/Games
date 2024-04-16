import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

name = input('What is your name?: ').upper()
name_char_list = [char for char in name]

# TODO 1: Create a dictionary
phonetic_word = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_word)

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
user_code = [phonetic_word[value] for value in name_char_list]
print(user_code)

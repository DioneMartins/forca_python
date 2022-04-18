import os, random, json
folder_input = '.' + os.sep + 'word_bank' + os.sep
file_input = folder_input + 'word_bank.json' 

def word_adder(new_word):
    array_of_words = bank_extractor()
    if new_word not in array_of_words:
        bank = open(file_input, 'ab')
        will_add = new_word + '--'
        will_add = will_add.encode("UTF-8")
        bank.write(will_add)
        bank.close()

def word_getter():
    array_of_words = bank_extractor()
    index = random.randrange(0, len(array_of_words))
    chosen_word = array_of_words[index]
    return chosen_word

def bank_extractor():
    bank = open(file_input, 'r', encoding="utf-8")
    data = json.load(bank)
    bank.close()
    string_bank = data["wordbank"]
    return string_bank

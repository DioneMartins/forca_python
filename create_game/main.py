import os
from word_bank import word_bank_user

class Game:
    def main(self):
        self.reset_variables()
        self.get_user_given_word()
        self.play_game()
        self.end_or_restart_game()

    def reset_variables(self):
        self.game_word = ""
        self.real_word = ""
        self.final_message = ""
        self.is_playing = True
        self.max_errors = 10
        self.errors = 0
        self.blacked_out_word = "_"
        self.tried_letters = []

    # Game:

    def play_game(self):
        while self.is_playing:
            print("Erros: "+str(self.errors))
            print("Letras que já foram ditas: "+str(self.tried_letters))
            print(self.blacked_out_word)
            user_input = input("Sua letra: ").lower()
            user_input = self.transformer(user_input)
            self.clear_console()

            if len(user_input) > 1:
                self.errors = self.errors + 1
                print("Uh-oh, trapaceiro perde ponto!\n")
            elif len(user_input) < 1:
                print("Tente inserir uma letra\n")
            elif user_input in self.blacked_out_word:
                print("Essa letra já está na palavra\n")
            elif user_input in self.tried_letters:
                print("Você já tentou essa letra\n")
            else:
                self.check_if_got_point(user_input)
            
            # End game
            if self.errors==self.max_errors:
                self.is_playing = False
                self.final_message = "Você perdeu"
            elif self.blacked_out_word == self.real_word:
                self.is_playing = False
                self.final_message = "Parabéns, você descobriu a palavra!"

    def end_or_restart_game(self):
        print(self.final_message)
        print("Gostaria de jogar de novo? [s/n]")
        user_input = input().lower()
        if user_input == "s":
            self.main()

    # Checking user input:

    def check_if_got_point(self, user_input):
        if user_input in self.game_word:
            print("Correto!\n")
            # Used for loop instead of find() to get multiple instances
            for index, letter in enumerate(self.game_word):
                if letter == user_input:
                    listed_blacked_out_word = list(self.blacked_out_word)
                    listed_blacked_out_word[index] = self.real_word[index]
                    self.blacked_out_word="".join(listed_blacked_out_word)
        else:
            self.errors = self.errors + 1
            print("Menos um ponto!\n")
            self.tried_letters.append(user_input)

    # Setting word and checking:

    def get_user_given_word(self):
        question_unanswered = True
        while question_unanswered:
            print("Você gostaria de inserir uma palavra? [s/n]")
            user_input = input().lower()
            if user_input == "s":
                user_input = input("Insira a palavra: ").lower()
                if user_input.isalpha():
                    self.game_word = user_input
                    self.add_user_word_to_bank(user_input)
                    self.blacked_out_word = len(user_input)*"_"
                    question_unanswered = False
                    self.do_accent_check()
                    print("Pressione enter para começar")
                    input()
                    self.clear_console()
                else:
                    print("A palavra não pode conter caracteres especiais - mesmo hífen")
            elif user_input == "n":
                print("Então aguarde enquanto puxamos uma palavra do nosso banco")
                question_unanswered = False
                self.get_random_word()
            else:
                print("Favor inserir uma resposta válida")

    # Formatting:

    def do_accent_check(self):
        accent_array = set(["á","à","ã","â","é","è","ê","í","ì","î","õ","ó","ò","ô","ú","ù","û"])
        setted_word = set(self.game_word)
        accented_letters = list(accent_array.intersection(setted_word))
        self.real_word = self.game_word
        if accented_letters:
            for item in accented_letters:
                new_vowel = self.transformer(item)
                position = self.game_word.find(item)
                listed_word = list(self.game_word)
                listed_word[position] = new_vowel
                self.game_word="".join(listed_word)

    def transformer(self, item):
        if item in ["á","à","ã","â"]:
            return "a"
        elif item in ["é","è","ê"]:
            return "e"
        elif item in ["í","ì","î"]:
            return "i"
        elif item in ["õ","ó","ò","ô"]:
            return "o"
        elif item in ["ú","ù","û"]:
            return "u"
        elif item.isalpha():
            return item
        else:
            return ""

    # Word bank and picking:

    def get_random_word(self):
        my_word = word_bank_user.word_getter()
        self.game_word = my_word
        self.blacked_out_word = len(my_word)*"_"
        self.do_accent_check()
        print("Pressione enter para começar")
        input()
        self.clear_console()
    
    def add_user_word_to_bank(self, user_word):
        word_bank_user.word_adder(user_word)


    # Other:

    def clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

if __name__ == "__main__":
    Game().main()
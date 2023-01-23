import os
from vocabulary import get_word_to_guess, get_words_from_string, all_words_str, word_length
from check_word import word_in_vocab, construct_word
from output import format_word_for_print
from user_input import sanitize_input, translation_tup
import colorama

round_fore: str = colorama.Fore.BLUE
round_back: str = colorama.Back.RESET
reset_fore: str = colorama.Fore.RESET
reset_back: str = colorama.Back.RESET
error_fore: str = colorama.Fore.RED
positive_fore: str = colorama.Fore.GREEN

def format_board_for_print(already_guessed: list[str]) -> str:
    board: str = ''

    for i, word in enumerate(already_guessed):
        line: str = f"{round_back}{round_fore}{i+1}{reset_back}{reset_fore} {word}"
        board = f"{board}\n{line}"

    return board


rounds: int = 6
current_round: int = 0
all_words_list = get_words_from_string(words_in_string=all_words_str, word_length=word_length)
word_to_guess = get_word_to_guess(all_words_list)
already_guessed_words: list[str] = []
unknown_word: bool = False
won: bool = False
words_guessed: list[str] = []

while (current_round < rounds) and not won:
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("hadane slovo: ", word_to_guess)
    first_line: str = f"{error_fore}Toto slovo neni zname!{reset_fore}" if unknown_word else ""
    print(first_line)
    board: str = format_board_for_print(already_guessed=already_guessed_words)
    print(board)


    guessed_word = input("Zadej hadane slovo: ")
    guessed_word = sanitize_input(word=guessed_word, replace=translation_tup)
    unknown_word = not(word_in_vocab(word=guessed_word, vocab=all_words_list))
    if not unknown_word:
        guessed_word_tup = construct_word(word_to_guess=word_to_guess, guessed_word=guessed_word,
                                          word_length=word_length)
        formatted_guessed_word = format_word_for_print(word_to_print=guessed_word_tup)
        already_guessed_words.append(formatted_guessed_word)
        current_round +=1
        if guessed_word == word_to_guess:
            won = True
        unknown_word = False
    else:
        unknown_word = True
    # clear


if won:
    final_text = f"{positive_fore}Vyhral/a jsi!{reset_fore}\n" \
                 f"{reset_fore}Hledane slovo bylo: {round_fore}{word_to_guess}{reset_fore}"
else:
    final_text = f"{error_fore}Prohral/a jsi!\n" \
                 f"{reset_fore}Hledane slovo bylo: {round_fore}{word_to_guess}{reset_fore}"

os.system('cls' if os.name == 'nt' else 'clear')
print()
board: str = format_board_for_print(already_guessed=already_guessed_words)
print(board)
print(final_text)
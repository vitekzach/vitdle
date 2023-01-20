from vocabulary import all_words_str, get_words_from_string, word_length
from check_word import construct_word, word
from output import format_word_for_print

all_words_list: list[str] = get_words_from_string(words_in_string=all_words_str, word_length=word_length)

word_tup: word = construct_word(word_to_guess='zmije', guessed_word='zmyje', word_length=word_length)

print(word_tup)
print(format_word_for_print(word_to_print=word_tup))




import colorama

x = f"{colorama.Fore.GREEN}so{colorama.Back.WHITE}me{colorama.Fore.YELLOW}t{colorama.Back.RESET}hi{colorama.Fore.RESET}ng"
print(x)

print(type(colorama.Fore.GREEN))
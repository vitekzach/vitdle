from check_word import word, letter
import colorama


def format_letter_for_print(letter_to_print: letter) -> str:
    formatted_letter: str = f"{letter_to_print.foreground_col}{letter_to_print.background_col}{letter_to_print.letter}" \
                            f"{colorama.Fore.RESET}{colorama.Back.RESET}"
    return formatted_letter


def format_word_for_print(word_to_print: word) -> str:
    formatted_word: str = f"{format_letter_for_print(letter_to_print=word_to_print.first)}" \
                          f"{format_letter_for_print(letter_to_print=word_to_print.second)}" \
                          f"{format_letter_for_print(letter_to_print=word_to_print.third)}" \
                          f"{format_letter_for_print(letter_to_print=word_to_print.fourth)}" \
                          f"{format_letter_for_print(letter_to_print=word_to_print.fifth)}"

    return formatted_word

from collections import namedtuple
from vocabulary import word_length
from color_letters import col_correct_let_bck, col_correct_pos_frn, col_correct_let_frn, col_correct_pos_bck, \
    col_other_bck, col_other_frn

# TODO move to separate script
word = namedtuple('word', ['first', 'second', 'third', 'fourth', 'fifth', 'whole', 'correct'])
letter = namedtuple('letter', ['letter', 'correct_position', 'in_final_word', 'foreground_col', 'background_col'])


def word_in_vocab(word: str, vocab: list[str]) -> bool:
    if word in vocab:
        return True
    return False


def construct_letter(letter_to_construct: str, letter_position: int, word_to_guess: str) -> letter:
    correct_position: bool = letter_to_construct == word_to_guess[letter_position]
    in_final_word: bool = letter_to_construct in word_to_guess
    foreground_color: str
    background_color: str

    if correct_position:
        foreground_color = col_correct_pos_frn
        background_color = col_correct_pos_bck
    elif in_final_word:
        foreground_color = col_correct_let_frn
        background_color = col_correct_let_bck
    else:
        foreground_color = col_other_frn
        background_color = col_other_bck

    letter_tup: letter = letter(letter=letter_to_construct,
                                correct_position=correct_position,
                                in_final_word=in_final_word,
                                # TODO add colours
                                foreground_col=foreground_color,
                                background_col=background_color)

    return letter_tup


def construct_word(word_to_guess: str, guessed_word: str, word_length: int) -> word:
    words: list[letter] = []

    for i in range(word_length):
        words.append(construct_letter(letter_to_construct=guessed_word[i], letter_position=i,
                                      word_to_guess=word_to_guess))

    word_tup = word(first=words[0], second=words[1], third=words[2], fourth=words[3], fifth=words[4],
                    whole=guessed_word, correct=guessed_word == word_to_guess)

    return word_tup

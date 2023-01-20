from collections import namedtuple
from vocabulary import word_length

word = namedtuple('word', ['first', 'second', 'third', 'fourth', 'fifth', 'whole', 'correct'])
letter = namedtuple('letter', ['correct_position', 'in_final_word', 'foreground_col', 'background_col'])


def word_in_vocab(word: str, vocab: list[str]) -> bool:
    if word in vocab:
        return True
    return False


def construct_letter(letter_to_construct: str, letter_position: int, word_to_guess: str) -> letter:
    letter_tup: letter = letter(correct_position=letter_to_construct == word_to_guess[letter_position],
                                in_final_word=letter_to_construct in word_to_guess,
                                # TODO add colours
                                foreground_col=None,
                                background_col=None)

    return letter_tup


def construct_word(word_to_guess: str, guessed_word: str, word_length: int) -> word:
    words: list[letter] = []

    for i in range(word_length):
        words.append(construct_letter(letter_to_construct=guessed_word[i], letter_position=i,
                                      word_to_guess=word_to_guess))

    word_tup = word(first=words[0], second=words[1], third=words[2], fourth=words[3], fifth=words[4],
                    whole=guessed_word, correct=guessed_word == word_to_guess)

    return word_tup
from collections import namedtuple

translator = namedtuple('Translator', ['trans_from', 'trans_to'])

translation_tup = (
    translator(trans_from='ě', trans_to='e'),
    translator(trans_from='š', trans_to='s'),
    translator(trans_from='č', trans_to='c'),
    translator(trans_from='ř', trans_to='r'),
    translator(trans_from='ž', trans_to='z'),
    translator(trans_from='ý', trans_to='y'),
    translator(trans_from='á', trans_to='a'),
    translator(trans_from='í', trans_to='i'),
    translator(trans_from='é', trans_to='e'),
    translator(trans_from='ó', trans_to='o'),
    translator(trans_from='ú', trans_to='u'),
    translator(trans_from='ů', trans_to='u'),
)


def sanitize_input(word: str, replace: tuple[translator]) -> str:
    word = word.lower()
    for replacement in replace:
        word = word.replace(replacement.trans_from, replacement.trans_to)

    return word


# def check_input(word: str, replace: tuple[translator], word_length: int) ->
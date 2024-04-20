"""
In this file I implemented target game for ukrainian words.
The file consist of 5 function for game implementation.
"""
import random
import time
from timeit import default_timer as timer
from memory_profiler import profile


def generate_grid() -> list[list[str]]:
    """
    () -> list[list[str]]
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    >>> random.seed(15)
    >>> generate_grid()
    ['й', 'а', 'в', 'и', 'л']
    """
    string_alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return random.sample(string_alphabet, 5)


def get_words(enter_file: str, letters: list[str]) -> list[str]:
    """
    (str, list[str]) -> list[str]
    Reads the file f. Checks the words with rules and returns a list of words.

    >>> get_words('base.lst', ['ґ', 'ь', 'й', 'є', 'ї'])
    [('ґалій', 'noun'), ('ґедзь', 'noun'), ('ґлей', 'noun'), ('ґудзь', 'noun'), \
('єврей', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), ('єресь', 'noun'), \
('їдець', 'noun'), ('їдкий', 'adjective'), ('їнь', 'noun'), \
('їхній', 'adjective'), ('йодль', 'noun')]
    """
    result = []

    with open(enter_file, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.strip().lower().split()
            if len(word[0]) <= 5 and (word[0][0] in letters) and (word[0][-1] in letters):
                if "/adj" in word[1]:
                    result.append((word[0], "adjective"))
                elif "/n" in word[1] or "noun" in word[1]:
                    result.append((word[0], "noun"))
                elif "/v" in word[1]:
                    result.append((word[0], "verb"))
                elif word[1][:3] == "adv" or word[1] == "adv":
                    result.append((word[0], "adverb"))
    return result


def get_user_words() -> list[str]:
    """
    () -> list[str]
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_list = []
    try:
        while True:
            user_input = input(">>> ")

            user_list.append(user_input)
    except EOFError:
        return user_list


def check_user_words(user_words: list[str],
                     language_part: str,
                     letters: list[str],
                     vocabulary: str) -> tuple[list[str]]:
    """
    (list[str], str, list[str], str)
    The function checks the user's word list against the 
    passed language part, the list of letters, and the list of pairs 
    (word, language part) in the vocabulary file.
    It returns a list of correct words of the user according to the 
    rules and the dictionary, and a list of words that the user missed.
    >>> check_user_words(['єресь', 'їхній', 'ґай'], 'noun', ['ґ', 'ь', 'й', 'є', 'ї'], 'base.lst')
    (['єресь'], ['ґалій', 'ґедзь', 'ґлей', 'ґудзь', 'єврей', 'єлей', 'їдець', 'їнь', 'йодль'])
    """
    vocabulary_ = get_words(vocabulary, letters=letters)
    right_words = []
    skipped_words = []

    for word in vocabulary_:
        if word[1] == language_part and word[0] in user_words:
            right_words.append(word[0])
            continue
        elif word[1] == language_part:
            skipped_words.append(word[0])
    return right_words, skipped_words


@profile
def main():
    """
    () -> None
    The main grid of taget game for Ukrainian words.
    The function unite all fanctions and display massages for users.
    """
    print("Пограймо в гру!")
    print()
    print("Придумай якомога більше слів, що мають не більше 5 літер\nта \
починаються і закінчуються на одну з наступних літер:")
    grid = generate_grid()
    print(grid)
    chastiny_movy = ['noun', 'verb', 'adjective', 'adverb']
    language_part = random.choice(chastiny_movy)
    print(f"Твої слова мають бути такою частиною мови {language_part}")
    user_words = get_user_words()
    print(f"Твої слова: {user_words}")
    right_words, skipped_words = check_user_words(
        user_words, language_part, grid, 'base.lst')
    print(f"Правильні слова {right_words}")
    print(f"Пропущені слова {skipped_words}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

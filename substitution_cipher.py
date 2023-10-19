import unicodedata

def unicode_to_ascii(unicode_text: str):
    return unicodedata.normalize('NFD', unicode_text).encode('ascii', 'ignore').decode('ascii')

ASCII_TABLE = [chr(i) for i in range(0, 127)]

def substitution_cipher(text: str, offset: int):
    return "".join([ASCII_TABLE[(ord(i)+offset)%127] for i in text])

def substitution_decipher(text: str, offset: int):
    return "".join([ASCII_TABLE[(ord(i)-offset)%127] for i in text])

FREQUENCY_CZECH = {
    " ": 1,
    "a": 0.09589269,
    "b": 0.0177612,
    "c": 0.02999077,
    "d": 0.03774841,
    "e": 0.10904081,
    "f": 0.0017506,
    "g": 0.00219812,
    "h": 0.02497482,
    "i": 0.06686138,
    "j": 0.02305759,
    "k": 0.03528082,
    "l": 0.05720782,
    "m": 0.0360545,
    "n": 0.05917244,
    "o": 0.08029999,
    "p": 0.03114961,
    "q": 0.00005933,
    "r": 0.04396827,
    "s": 0.0558597,
    "t": 0.05385289,
    "u": 0.03579031,
    "v": 0.03952464,
    "w": 0.00054266,
    "x": 0.0003591,
    "y": 0.02857512,
    "z": 0.03302643
}

char_frequency_czech_sorted = sorted(FREQUENCY_CZECH.items(), key=lambda x:x[1], reverse=True)
chars_by_frequency_czech = list(map(lambda x: x[0], char_frequency_czech_sorted))

def get_char_frequency_sorted(text: str) -> list:
    char_frequency = {}
    for char in text:
        try:
            char_frequency[char] += 1
        except:
            char_frequency[char] = 1
    return sorted(char_frequency.items(), key=lambda x:x[1], reverse=True)

def analyze_frequency_and_score_text(text: str) -> int:
    """
    Score is decided by:
    how close the order of the characters in the array sorted by frequency from the text 
    is to the order of the characters in the array sorted by frequency in Czech. 
    """
    chars_by_frequency = list(map(lambda x: x[0], get_char_frequency_sorted(text)))
    score = 0
    for i, char in enumerate(chars_by_frequency_czech):
        if char in chars_by_frequency:
            dist = abs(chars_by_frequency.index(char)-i)
            score += 127 - dist
    return score

def analyze_frequency_and_guess(text: str, only_best: bool=True) -> list|str:
    """
    Do frequency analysis on the cipher text and attempt to break it.

    Parameters:
    text (str): cipher text to break
    only_best (bool): 
        True: only return best guess
        False: return all guesses

    Returns:
    str|list: str if only_best is True otherwise list

    Weakpoints:
    Algorithm performs badly on:
    - very short texts, especially including uncommon letters for Czech (shorter than 10 characters)
    - texts without repeating characters
    - texts with many repeating non-alpha characters
    """

    char_frequency = get_char_frequency_sorted(text)
    best_guess = {
        "score": 0,
        "text": "",
        "offset": -1
    }
    guesses = []
    for i in range(10):
        offset_guess = 127 + ord(char_frequency[0][0]) - ord(char_frequency_czech_sorted[i][0]) % 127
        text_guess = substitution_decipher(text, offset_guess)
        score = analyze_frequency_and_score_text(text_guess)
        if not only_best:
            guesses.append(
                {
                    "score": score,
                    "text": text_guess,
                    "offset": offset_guess,
                    "most_common_char": char_frequency_czech_sorted[i][0]
                }
            )
        elif score > best_guess["score"]:
            best_guess = {
                "score": score,
                "text": text_guess,
                "offset": offset_guess
            }
    if only_best:
        return best_guess
    else:
        return sorted(guesses, key=lambda x: x["score"], reverse=True)

def print_demo(text: str):
    print(f"TEXT:\n{unicode_to_ascii(text)}")

    offset = 47
    cipher_text = substitution_cipher(unicode_to_ascii(text), offset)
    print("CIPHER OFFSET:", offset)
    print(f"CIPHER TEXT:\n{cipher_text.encode('ascii')}\n")
    guesses = analyze_frequency_and_guess(cipher_text, only_best=False)
    print("GUESSES:")
    print(*guesses, sep="\n")
    best_guess = guesses[0]
    print(f"\nBEST GUESS - score: {best_guess['score']}, offset (key): {best_guess['offset']}:\n{best_guess['text']}")

if __name__ == "__main__":
#     text = """
# Epos o Gilgamešovi (rozbor)
# Kanonická verze eposu vznikla koncem druhého tisíciletí př.n.l., ale jeho kořeny jsou mnohem starší. Jeho verze v různých jazycích byly známy po celém Předním východě. Text kanonické verze Eposu o Gilgamešovi se nám zachoval především ve svém akkadském zápise v knihovně krále Aššurbanipala v Ninive (7. století př.n.l.).
#     """
    text = "Toto je test."
    # text = "strčprstskrzkrk"
    print_demo(text)
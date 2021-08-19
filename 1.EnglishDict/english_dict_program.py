import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

# finding max ratio between the 3 possibilities: lower, upper and original word
def find_max_ratio(word):
    word_lowered = word.lower()
    word_upper = word.upper()
    lst_close = get_close_matches(word,data.keys(),cutoff=0.7)
    lst_close_lower = get_close_matches(word_lowered,data.keys(),cutoff=0.7)
    lst_close_upper = get_close_matches(word_upper,data.keys(),cutoff=0.7)

    ratio ,ratio_lower,ratio_upper = 0, 0, 0
    if len(lst_close) != 0 : ratio = SequenceMatcher(None,lst_close[0],word).ratio()
    if len(lst_close_lower) != 0 : ratio_lower = SequenceMatcher(None,lst_close_lower[0],word_lowered).ratio()
    if len(lst_close_upper) != 0 : ratio_upper = SequenceMatcher(None,lst_close_upper[0],word_upper).ratio()

    max_ratio = max(ratio,ratio_lower,ratio_upper)
    if max_ratio < 0.8 :
        return None
    if ratio == max_ratio :
        return lst_close[0]
    elif ratio_lower == max_ratio :
        return lst_close_lower[0]
    else:
        return lst_close_upper[0]

def get_translation(word):
    word_lowered = word.lower()
    word_upper = word.upper()

    if word in data:
        return data[word]
    elif word_lowered in data:
        return data[word_lowered]
    elif word_upper in data:
        return data[word_upper]
    else :
        closest_word = find_max_ratio(word)

        if closest_word is None:
            return "Sorry ... The word is not in the dictionary"
        else :
            answer = input(f"Did you mean {closest_word} ? If yes please type Y:\n")
            if answer == "Y" :
                return data[closest_word]
            else:
                return "Sorry ... The word is not in the dictionary"

def print_def(translation_lst):
    if type(translation_lst) != str:
        i = 1
        for temp in translation_lst:
            print("Definition ",i," : ", temp)
            i = i + 1
    else:
         print(translation_lst)

word_input = input("Enter a word: ")

print_def(get_translation(word_input))



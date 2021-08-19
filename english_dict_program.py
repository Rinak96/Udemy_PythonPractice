import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def get_translation(word,case_sensitive = False):
    word_lowered = ""
    if not case_sensitive :
        word_lowered = word.lower()
    if word_lowered in data:
        return data[word_lowered]
    elif word in data:
        return data[word]
    else:
        if case_sensitive:
            return ""
        else:
            originial_translation = get_translation(word,True)
            if len(originial_translation) > 0:
                return originial_translation

            lst_close = get_close_matches(word_lowered,data.keys(),cutoff=0.7)

            if len(lst_close) == 0:
                return "Sorry ... The word is not in the dictionary"
            else :
                answer = input(f"Did you mean {lst_close[0]} ? If yes please type Y:\n")
                if answer == "Y" :
                    return data[lst_close[0]]
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



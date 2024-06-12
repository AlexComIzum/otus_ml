from re import search

UNDERSCORE = "_"


def change_word(sentence):
    result = ""
    if search(UNDERSCORE, sentence):
        result = change_up_registr(sentence)
    else:
        result = change_low_registr(sentence)
    return result


def change_up_registr(sentence):
    result_sentence = ""
    index_sentence = 0
    print("Check 1")
    for symvol in sentence:
        curr_symvol = ""
        if index_sentence == 0:
            symvol = symvol.upper()
            result_sentence += symvol
        index_sentence += 1
        if symvol != UNDERSCORE and index_sentence > 1:
            result_sentence += symvol
        elif symvol == UNDERSCORE:
            index_sentence = 0

    return result_sentence


def change_low_registr(sentence):
    result_sentence = ""
    index_sentence = 0
    print("Check 2")
    for symvol in sentence:
        curr_symvol = ""
        if symvol.isupper() and index_sentence == 0:
            result_sentence += symvol.lower()
        elif symvol.isupper():
            result_sentence += UNDERSCORE + symvol.lower()
        else:
            result_sentence += symvol.lower()
        index_sentence += 1

    return result_sentence


worlds = input()
result_worlds = change_word(worlds)
print(result_worlds)

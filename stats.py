from typing import List

def dic_to_list(dictionary: dict[str, int]) -> List[dict[str, int | str]]:
    list_of_keys = list(filter(lambda key: key.isalpha(), dictionary))
    return list(map(lambda char: {"char": char, "num": dictionary[char]}, list_of_keys))

def get_num_words(content: str) -> str:
    count = len(content.split())

    return f"Found {count} total words"

def get_chars_counts(content: str) -> dict[str, int]:
    chars_counts = dict()

    for chr in content:
        char = chr.lower()

        if char in chars_counts:
            chars_counts[char] += 1
        else: 
            chars_counts[char] = 1

    return chars_counts

def sort_dict_list(dictionnary: dict) -> List[dict[str, str | int]]:
    list_of_dics = dic_to_list(dictionnary)
    list_of_dics.sort(reverse=True, key=lambda char_stat: char_stat["num"])

    return list_of_dics
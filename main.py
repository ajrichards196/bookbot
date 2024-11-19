def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_text_from_file(path_to_file)
    num_words = count_words_in_string(text)
    num_chars = count_chars(text)
    num_list = sort_dict(num_chars)
    print(f"--- Begin report of {path_to_file}")
    print(f"{num_words} words found in the document")
    for item in num_list:
        print(f"The character {item['char']} appears {item['num']} times")
    



def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()
    

def count_words_in_string(text_string):
    words = text_string.split()
    return len(words)


def count_chars(text_string):
    chars = {}
    for char in text_string:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(d):
    list_dicts = []
    for key in d:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = d[key]
        list_dicts.append(new_dict)
    def sort_on(dict):
        return dict["num"]
    order_list = list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts



main()



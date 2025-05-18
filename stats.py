def num_of_words(text):
    words = text.split()
    number = len(words)
    return number

def count_char(text):

    text = text.lower()
    char = {}

    for i in text:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
        
    return char

def list_to_sort(dict):

    sorted_list = []
    for i in dict:
        sorted_list.append({"char": i, "num": dict[i]})
    
    sorted_list.sort(reverse=True, key=to_sort)

    return sorted_list

def to_sort(dict):
    return dict["num"]
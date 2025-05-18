import sys
from stats import num_of_words, count_char, list_to_sort

def get_book_text(path_of_file):
    with open(path_of_file) as f:
        text = f.read()
        return text
    

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_of_file = sys.argv[1]
    text = get_book_text(path_of_file)
    number_of_words = num_of_words(text)
    characters_dic = count_char(text)
    sorted_list = list_to_sort(characters_dic)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_file}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
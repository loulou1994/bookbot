import sys
from stats import get_num_words, get_chars_counts, sort_dict_list

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text_content = get_book_text(file_path)
    word_count = get_num_words(text_content)
    counts_of_chars = get_chars_counts(text_content)
    list_of_dics = sort_dict_list(counts_of_chars)

    print_report(word_count, file_path, list_of_dics)

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

def print_report(word_counts, filename, chars_counts):
    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {filename}...")
    # print(word_counts)
    # print("----------- Word Count ----------")
    for item in chars_counts[:2]:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    # print("============= END ===============")

main()
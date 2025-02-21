def main():
    lowercase_words = {}
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()

    for char in file_contents:
        if char not in lowercase_words:
            lowercase_words[char] = 1
        else:
            lowercase_words[char] += 1

    list_of_dicts = [{'char': key, 'count': value} for key, value in lowercase_words.items() if key.isalpha()]

    sorted_list = sorted(list_of_dicts, key=lambda x: x['count'], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report of books/frankenstein.txt ---")
    
    
if __name__ == "__main__":
    main()

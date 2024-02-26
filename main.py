import sys

def get_book_content(book_path: str) -> str:
    with open(book_path, "r") as file:
        return file.read()
    
def get_book_words_count(book_content: str) -> int:
    return len(book_content.split())

def get_book_characters_count(book_content: str) -> dict:
    
    character_count = {}

    for character in book_content.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

def sort_on(dict) -> int:
    return dict['count']

def get_book_characters_dict_as_sorted_list(book_characters_count: dict) -> list:
    list_of_characters = []
    
    for character, count in book_characters_count.items():
       if character.isalpha():
           list_of_characters.append({"character": character, "count": count})

    list_of_characters.sort(key=sort_on, reverse=True)

    return list_of_characters

def main() -> int:
    
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)

    book_words_count = get_book_words_count(book_content)

    book_characters_count = get_book_characters_count(book_content)

    list_of_characters = get_book_characters_dict_as_sorted_list(book_characters_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book_words_count} words found in the document")
    print("")

    for character in list_of_characters:
        print(f"The '{character['character']}' character was found {character['count']} times")

    print(f"--- End report ---")

    return 0

if __name__ == "__main__":
    sys.exit(main())
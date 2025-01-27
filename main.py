def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    alpha_text = get_alpha_text(text)
    num_char = get_num_each_char(alpha_text)
    #Turning num char into a list and then sorting by number
    num_char_list = [{"char":k, "num":v} for k,v in num_char.items()]
    num_char_list.sort(reverse=True, key=sort_on)

    
    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    for char in num_char_list:
        print(f"The '{char['char']}' character appears {char['num']} times")
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_each_char(words):
    char_count = {}
    lower_words = words.lower()
    for word in lower_words:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(dict):
     return dict["num"]

def get_alpha_text(text):
    alpha_text = ""
    for char in text:
        if char.isalpha():
            alpha_text += char
    return alpha_text

# ##My code before the solution
#     #with open("books/frankenstein.txt") as f:

#         #file_contents = f.read()
#         ###printing the whole book
#         #print(file_contents)
#         ###printing how many words there are in the book
#         #words = file_contents.split()
#         #print(len(words))
#         #print(type(words))

#if __name__ == "__main__":
main()